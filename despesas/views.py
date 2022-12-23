from django.shortcuts import render, redirect, get_list_or_404
from .forms import DespesasForm
from .models import Despesas
from receitas.models import Receitas
import datetime
from django.http import JsonResponse
import requests
import json
from despesa_categoria.models import CategoriaDespesa
from receita_categoria.models import CategoriaReceita
# Create your views here.

def index(request):
    return render(request, 'despesas/index.html')

def formsadd(request):
    if request.method == 'GET':
        form = DespesasForm()
        return render(request,'despesas/create.html',{'form':form})
    if request.method == 'POST':
        form = DespesasForm(request.POST)
        if form.is_valid():
            form.save()
        form = DespesasForm()
        return render(request,'despesas/create.html',{'form':form})

def allDespesas(request):
    despesas = Despesas.objects.all()
    return render(request, 'despesas/despesas.html',{'despesas':despesas})

def editDespesa(request,id):
    despesa = get_list_or_404(Despesas,pk=id)
    form = DespesasForm(instance = despesa)
    if request.method == 'GET':
        return render(request,'despesas/edit.html',{'form':form})
    else:
        form = DespesasForm(request.POST, instance = despesa)
        if form.is_valid():
            form.save()
        return render(request,'despesas/edit.html',{'form':form})


def delete(request,id):
    despesa = get_list_or_404(Despesas,pk=id)
    despesa.delete()
    return redirect('/')

def despesasanuais(request):
    if request.method == 'GET':
        month = datetime.date.today().month
        ano = datetime.date.today().year
        list_mes = []
        for i in range(1,13):
            list_mes.append(i)

        meses = list_mes[0:month]

        x = Despesas.objects.all()
        sum = 0
        for i in x:
           if i.tipoDespesas == '1' and i.data.year == ano:
            sum = sum + i.value

        soma_final = []
        for i in meses:
            despesa_deste_mes = []
            for j in x:
                if i == j.data.month and ano == j.data.year:
                    despesa_deste_mes.append(j)
            if len(despesa_deste_mes) == 0:
                soma_final.append(sum)
            else:
                valores_eventuais = 0
                for i in despesa_deste_mes:
                    if i.tipoDespesas == '2':
                        valores_eventuais = valores_eventuais + i.value
                soma_final.append(valores_eventuais + sum)


        return JsonResponse({'mes':meses, 'valor mensal':soma_final})

def receitasanuais(request):
    if request.method == 'GET':
        month = datetime.date.today().month
        ano = datetime.date.today().year
        list_mes = []
        for i in range(1,13):
            list_mes.append(i)

        meses = list_mes[0:month]

        x = Receitas.objects.filter(data__year=ano)
        sum = 0
        for i in x:
           if i.tipoReceita == '1':
            sum = sum + i.valor

        soma_final = []
        for i in meses:
            receita_deste_mes = []
            for j in x:
                if i == j.data.month:
                    receita_deste_mes.append(j)
            if len(receita_deste_mes) == 0:
                soma_final.append(sum)
            else:
                valores_eventuais = 0
                for i in receita_deste_mes:
                    if i.tipoReceita == '2':
                        valores_eventuais = valores_eventuais + i.valor
                soma_final.append(valores_eventuais + sum)
        return JsonResponse({'mes':meses, 'valor mensal':soma_final})

def receitasvsdespesas(request):
    if request.method == 'GET':
        URL_despesas = 'http://localhost:8000/despesasanuais'
        URL_receitas = 'http://localhost:8000/receitasanuais'
        receitas = requests.get(URL_receitas)
        despesas = requests.get(URL_despesas)
        despesasJson = despesas.json()
        receitasJson = receitas.json()
        return JsonResponse({'receitas':receitasJson['valor mensal'],'despesas':despesasJson['valor mensal'], 'meses':despesasJson['mes']})

def categoriadespesa(request):
    if request.method == 'GET':
        categoriadespesa = CategoriaDespesa.objects.all()
        ano = datetime.date.today().month
        lista_despesas = []
        lista_valores = []
        for i in categoriadespesa:
            lista_valores.append(0)
        cont = 0
        for cd in categoriadespesa:
            lista_despesas.append(cd.name)
            despesas = cd.despesas_set.all()
            if len(despesas) > 0:
                for d in despesas:
                    lista_valores[cont] = lista_valores[cont] + d.value
            cont = cont + 1
        return JsonResponse({'categorias': lista_despesas,'valores': lista_valores})

def categoriareceita(request):
    if request.method == 'GET':
        categoriareceitas = CategoriaReceita.objects.all()
        ano = datetime.date.today().month
        lista_receitas = []
        lista_valores = []
        for i in categoriareceitas:
            lista_valores.append(0)
        cont = 0
        for cd in categoriareceitas:
            lista_receitas.append(cd.name)
            receitas = cd.receitas_set.all()
            if len(receitas) > 0:
                for d in receitas:
                    lista_valores[cont] = lista_valores[cont] + d.valor
            cont = cont + 1
        return JsonResponse({'categorias': lista_receitas,'valores': lista_valores})

def lucros(request):
    if request.method == "GET":
        URL_despesas = 'http://localhost:8000/despesasanuais'
        URL_receitas = 'http://localhost:8000/receitasanuais'
        receitas = requests.get(URL_receitas)
        despesas = requests.get(URL_despesas)
        despesasJson = despesas.json()
        receitasJson = receitas.json()
        lucro = []
        for i in range(len(despesasJson["mes"])):
            value = receitasJson["valor mensal"][i] - despesasJson["valor mensal"][i]
            lucro.append(value)
        return JsonResponse({"lucro":lucro,"meses":despesasJson["mes"]})
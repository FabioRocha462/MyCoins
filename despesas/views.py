from django.shortcuts import render, redirect
from .forms import DespesasForm
from .models import Despesas
from receitas.models import Receitas
import datetime
from django.http import JsonResponse
import requests
import json
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
    despesa = Despesas.objects.get(id = id)
    form = DespesasForm(instance = despesa)
    if request.method == 'GET':
        return render(request,'despesas/edit.html',{'form':form})
    else:
        form = DespesasForm(request.POST, instance = despesa)
        if form.is_valid():
            form.save()
        return render(request,'despesas/edit.html',{'form':form})


def delete(request,id):
    despesa = Despesas.objects.get(id=id)
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
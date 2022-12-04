from django.shortcuts import render,redirect
from .models import Receitas
from .forms import ReceitaSForm
import datetime
from django.http import JsonResponse
# Create your views here.

def receitaadd(request):
    if request.method == 'GET':
        form = ReceitaSForm()
        return render(request, 'receitas/create.html', {'form':form})
    if request.method == 'POST':
        form = ReceitaSForm(request.POST)
        if form.is_valid():
            form.save()
        form = ReceitaSForm()
        return render(request, 'receitas/create.html', {'form':form})

        
def allreceitas(request):
    receitas = Receitas.objects.all()
    return render(request, 'receitas/receitas.html',{'receitas':receitas})

def delete(request,id):
    receita = Receitas.objects.get(id=id)
    receita.delete()
    return redirect('/')

def edit(request,id):
    receita = Receitas.objects.get(id=id)
    form = ReceitaSForm(instance = receita)
    if request.method == 'GET':
        return render(request, 'receitas/edit.html', {'form':form})
    else:
        form = ReceitaSForm(request.POST, instance = receita)
        form.save()
        form = ReceitaSForm(instance = receita)
        return render(request, 'receitas/edit.html', {'form':form})


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


from django.shortcuts import render, redirect
from .forms import DespesasForm
from .models import Despesas
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
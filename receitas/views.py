from django.shortcuts import render,redirect
from .models import Receitas
from .forms import ReceitaSForm
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


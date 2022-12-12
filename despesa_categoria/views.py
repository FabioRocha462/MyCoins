from django.shortcuts import render, redirect
from .forms import CategoriaDespesaForm
from .models import CategoriaDespesa

# Create your views here.

def formadd(request):
    if request.method == 'GET':
        form = CategoriaDespesaForm()
        return render(request, 'despesa_categoria/create.html', {'form': form})
    if request.method == 'POST':
        form = CategoriaDespesaForm(request.POST)
        if form.is_valid():
            form.save()
        form = CategoriaDespesaForm()
        return render(request, 'despesa_categoria/create.html', {'form': form})

def index(request):
    if request.method == 'GET':
        categoriadespesas = CategoriaDespesa.objects.all()
        return render(request, 'despesa_categoria/despesa_categoria.html', {'categoriadespesas': categoriadespesas})

def delete(request,id):
    categoriadespesa = CategoriaDespesa.objects.get(id = id)
    categoriadespesa.delete()
    return redirect('/')

def edit(request,id):
    categoriadespesa = CategoriaDespesa.objects.get(id = id)
    form = CategoriaDespesaForm(instance  = categoriadespesa)
    if request.method == 'GET':
        return render(request,'despesa_categoria/edit.html',{'form':form})
    if request.method == 'POST':
        form = CategoriaDespesaForm(request.POST, instance = categoriadespesa )
        if form.is_valid():
            form.save()
        return render(request,'despesa_categoria/edit.html',{'form':form})



        





from django.shortcuts import render,redirect
from .forms import CategoriaReceitaForm
from .models import CategoriaReceita
# Create your views here.

def formadd(request):
    if request.method == "GET":
        form = CategoriaReceitaForm()
        return render(request, 'receita_categoria/create.html', {'form':form})
    if request.method == "POST":
        form = CategoriaReceitaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'receita_categoria/create.html', {'form':form})

def index(request):
    categoria_receitas = CategoriaReceita.objects.all()
    return render(request, 'receita_categoria/receita_categoria.html', {'crs': categoria_receitas})

def delete(request,id):
    cr = CategoriaReceita.objects.get(id=id)
    cr.delete()
    return redirect('/')

def edit(request, id):
    cr = CategoriaReceita.objects.get(id=id)
    if request.method == "GET":
        form = CategoriaReceitaForm(instance = cr)
        return render(request, 'receita_categoria/edit.html', {'form':form})
    if request.method == "POST":
        form = CategoriaReceitaForm(request.POST,instance = cr)
        if form.is_valid():
            form.save()
        return render(request, 'receita_categoria/edit.html', {'form':form})
        




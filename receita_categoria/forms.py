from django import forms

from .models import CategoriaReceita

class CategoriaReceitaForm(forms.ModelForm):

    class Meta:
        model = CategoriaReceita
        fields = "__all__"
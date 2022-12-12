from django import forms
from .models import CategoriaDespesa

class CategoriaDespesaForm(forms.ModelForm):
    
    class Meta:
        model = CategoriaDespesa
        fields = '__all__'
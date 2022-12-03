from django import forms
from .models import Receitas

class ReceitaSForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = '__all__'
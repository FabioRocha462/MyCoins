from django import forms
from .models import Despesas

class DespesasForm(forms.ModelForm):

    class Meta:
        model = Despesas
        fields = '__all__'
        
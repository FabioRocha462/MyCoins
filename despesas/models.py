from django.db import models
from despesa_categoria.models import CategoriaDespesa
# Create your models here.

class Despesas(models.Model):
    tipo = (
        ('1', 'mensal'),
        ('2', 'eventual'),
    )

    name = models.CharField(max_length=255)
    value  = models.FloatField()
    tipoDespesas = models.CharField(
        max_length=1,
        choices=tipo,
    )
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now = True)
    categoria = models.ForeignKey(CategoriaDespesa, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True)

    
    def __str__(self):
        return self.name
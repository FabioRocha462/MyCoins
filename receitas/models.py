from django.db import models

# Create your models here.

class Receitas(models.Model):
    tipo = (
        ('1', 'mensal'),
        ('2','eventual'),
    )
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    tipoReceita = models.CharField(
        max_length=1,
        choices=tipo,
    )
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome
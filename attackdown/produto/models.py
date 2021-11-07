from django.db import models

# Create your models here.
class Produto(models.Model):
    produto_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=90)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default=0.01)
    quantidade = models.IntegerField()
    peso = models.DecimalField(decimal_places=3, max_digits=5)
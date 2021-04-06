from django.db import models
from account.models import Account

# Create your models here.
class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    nomeFuncionario = models.ForeignKey(Account, default=None, on_delete=models.DO_NOTHING, null=True)
    dataPedido = models.DateField()
    status = models.BooleanField()
    valorTotal = models.DecimalField(max_digits=7, decimal_places=2)
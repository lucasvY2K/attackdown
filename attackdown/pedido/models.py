from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel

from cliente.models import Cliente
from produto.models import Produto


class Pedido(TimeStampedModel):
    cnpj = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Pedido{self.id}"


class Item(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="items", on_delete=models.CASCADE)
    produto = models.ForeignKey(
        Produto, related_name="order_items", on_delete=models.CASCADE
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(settings.CARRINHO_ITEM_MAX_QUANTIDADE),
        ]
    )

    def __str__(self):
        return str(self.id)
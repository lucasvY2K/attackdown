from django import forms
from .models import Pedido
from account.models import Account
from produto.models import Produto
import datetime
from django.forms import ModelChoiceField

class ProdutoModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class PedidoForm(forms.ModelForm):
    nomeFuncionario = forms.ModelChoiceField(queryset=Account.objects.all(), widget=forms.HiddenInput(), required=False)
    dataPedido = forms.DateField(initial=datetime.date.today)
    status = forms.BooleanField(initial=True, required=False)
    produto = ProdutoModelMultipleChoiceField(queryset=Produto.objects.all())
    quantidade = forms.IntegerField(min_value=1)
    class Meta:
        model = Pedido
        fields = ("nomeFuncionario", "dataPedido", "status", "quantidade", "produto")

class EditarPedido(forms.ModelForm):
    status = forms.BooleanField(initial=False, required=False)
    quantidade = forms.IntegerField(min_value=1)

    class Meta:
        model = Pedido
        fields = ("status", "quantidade")
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
    valorTotal = forms.DecimalField(initial=0.10)
    produto = ProdutoModelMultipleChoiceField(queryset=Produto.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Pedido
        fields = ("nomeFuncionario", "dataPedido", "status", "valorTotal", "produto")

class EditarPedido(forms.ModelForm):
    status = forms.BooleanField(initial=False, required=False)
    valorTotal = forms.DecimalField(initial=0.10)

    class Meta:
        model = Pedido
        fields = ("status", "valorTotal")
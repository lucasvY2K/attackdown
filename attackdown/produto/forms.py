from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    nome = forms.CharField()
    descricao = forms.CharField()
    preco = forms.DecimalField(min_value=0.00, initial=0.01)
    quantidade = forms.IntegerField(min_value=1, initial=0)
    peso = forms.DecimalField(min_value=0.0, initial=0.1)

    class Meta:
        model = Produto
        fields = ("nome", "descricao", "preco", "quantidade", "peso")
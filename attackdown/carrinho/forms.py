from django import forms
from django.conf import settings

PRODUTO_QUANTIDADE_ESCOLHAS = [
    (i, str(i)) for i in range(1, settings.CARRINHO_ITEM_MAX_QUANTIDADE + 1)
]

class CarrinhoAddProdutoForm(forms.Form):
    quantidade = forms.TypedChoiceField(choices=PRODUTO_QUANTIDADE_ESCOLHAS, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

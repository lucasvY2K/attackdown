from django import forms
from django.db.models import fields
from .models import Cliente

class ClienteForm(forms.ModelForm):
    cnpj = forms.CharField(
        widget=forms.TextInput(attrs={'name':'cnpj','id':'cnpj'})
    )
    nome = forms.CharField()
    email = forms.CharField()
    endereco = forms.CharField()
    telefone = forms.CharField()

    class Meta:
        model = Cliente
        fields = ("cnpj", "nome", "email", "endereco", "telefone")
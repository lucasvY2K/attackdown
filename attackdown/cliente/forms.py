from django import forms
from django.db.models import fields
from .models import Cliente

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField()
    nome = forms.CharField()
    email = forms.CharField()
    endereco = forms.CharField()
    telefone = forms.CharField()

    class Meta:
        model = Cliente
        fields = ("cpf", "nome", "email", "endereco", "telefone")
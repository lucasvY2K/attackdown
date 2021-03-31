from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from account.models import Account
from django.contrib.auth import authenticate
from attackdown import settings
from django.http import request

class AccountAuthenticationForm(forms.ModelForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email'] 
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Email e senha não combinam ou não estão cadastrados")

class RegistrationForm(UserCreationForm):
    cpf = forms.CharField(required=True, label='CPF',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'000.000.000-00', 'name':'cpf', 'id':'cpf'
        }))
    email = forms.EmailField(max_length=60, required=True, label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'email@email.com'
        }))
    nome = forms.CharField(max_length=35, required=True, label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'Nome e sobrenome'
        }))
    cargo = forms.CharField(max_length=35, required=True, label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control input-registro'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-registro',
                                                                  'placeholder':'8 digitos ou mais'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input-registro',
                                                                  'placeholder':'Ao menos uma letra'
        }))
    
    
    class Meta:
        model = Account
        fields = ("cpf", "email", "nome", "cargo", "password1", "password2")

class EditarFuncionarioForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, required=True, label='Email',
        widget=forms.EmailInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'email@email.com'
        }))
    nome = forms.CharField(max_length=35, required=True, label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control input-registro',
                                      'placeholder':'Nome e sobrenome'
        }))
    cargo = forms.CharField(max_length=35, required=True, label='Nome',
        widget=forms.TextInput(attrs={'class':'form-control input-registro'
        }))
    class Meta:
        model = Account
        fields = ("email", "nome", "cargo")

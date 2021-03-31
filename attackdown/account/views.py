from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.contrib import messages
from django.contrib.auth.models import AbstractUser  
from django.contrib.auth import login, authenticate, logout
from .models import Account
from .forms import AccountAuthenticationForm, RegistrationForm, EditarFuncionarioForm
from django import forms

# Create your views here.
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("/index")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("/index")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] =  form
    return render(request, 'registration/login.html', context)

def register(request):
    context = {}
    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            account.save()
            messages.success(request, 'Usuário cadastrado')
            return redirect("/accounts/register")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'registration/novo_user.html', context)

def logout_view(request):
    logout(request)
    return redirect("/accounts/login")

def exibir_funcionarios(request):
    usuario = request.user

    if usuario.is_authenticated:
        queryset = Account.objects.all()
        context = {
            'lista_funcionarios':queryset
        }
        return render(request, 'lista_funcionarios.html', context)
    else:
        return redirect("/")

def editar_funcionarios(request, cpf_funcionario):
    usuario = request.user
    funcionario = get_object_or_404(Account, cpf=cpf_funcionario)
    context = {}
    
    if not usuario.is_authenticated:
        return redirect("/")
    elif request.POST:
        editar_funcionario_form = EditarFuncionarioForm(request.POST, instance=funcionario)
        if editar_funcionario_form.is_valid():
            funcionario = editar_funcionario_form.save()
            funcionario.save()
            messages.success(request, 'Informações atualizadas')
            return redirect("/accounts/lista_funcionarios")
    else:
        editar_funcionario_form = EditarFuncionarioForm(instance=funcionario)
        context['editar_funcionario'] = editar_funcionario_form

    return render(request, 'editar_funcionario.html', context)


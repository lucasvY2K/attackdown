from django.forms.forms import Form
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Cliente

from .forms import ClienteForm

# Create your views here.
@login_required(login_url='/accounts/login')
def novo_cliente(request):
    context = {}
    cliente_form = ClienteForm(request.POST or None)
    if cliente_form.is_valid():
        cliente = cliente_form.save()
        cliente.save()
        cliente_form = Cliente()
        return redirect("/cliente/lista")
    context['cliente_form'] = cliente_form
    return render(request, 'cliente\cliente.html', context)

@login_required(login_url='/accounts/login')
def lista_clientes(request):
    queryset = Cliente.objects.all()
    context = {
        'clientes':queryset
    }
    return render(request, 'cliente\lista-clientes.html', context)

@login_required(login_url='/accounts/login')
def editar_cliente(request, cnpj_cliente):
    context = {}
    cliente = get_object_or_404(Cliente, cnpj=cnpj_cliente)
    if request.POST:
        editar_cliente_form = ClienteForm(request.POST, instance=cliente)
        if editar_cliente_form.is_valid():
            cliente = editar_cliente_form.save()
            cliente.save()
            return redirect("/cliente/lista")
    else:
        editar_cliente_form = ClienteForm(instance=cliente)
        context['cliente'] = editar_cliente_form
    return render(request, 'cliente\editar-cliente.html', context)

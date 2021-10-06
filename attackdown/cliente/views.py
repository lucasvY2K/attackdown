from django.forms.forms import Form
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render

from .models import Cliente

from .forms import ClienteForm

# Create your views here.
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

def lista_clientes(request):
    queryset = Cliente.objects.all()
    context = {
        'clientes':queryset
    }
    return render(request, 'cliente\lista-clientes.html', context)

def editar_cliente(request, cpf_cliente):
    context = {}
    cliente = get_object_or_404(Cliente, cpf=cpf_cliente)
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

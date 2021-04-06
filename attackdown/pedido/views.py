from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from .models import Pedido
from .forms import PedidoForm
from django.http import request

# Create your views here.
def criar_pedido(request):
    context = {}
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        pedido = form.save()
        pedido.nomeFuncionario = request.user
        pedido.save()
        form = Pedido()
        return redirect("/index")
    context['form'] = form
    return render(request, 'pedido.html', context)

def lista_pedidos(request):
    queryset = Pedido.objects.filter(nomeFuncionario=request.user).order_by('-status')
    context = {
        'pedidos':queryset
    }
    return render(request, 'lista-pedidos.html', context)
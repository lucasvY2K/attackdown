from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from carrinho import forms
from django.contrib.auth.decorators import login_required

from carrinho.carrinho import Carrinho
import produto
from produto.models import Produto

from .forms import PedidoCreateForm, FinalizaPedidoForm
from .models import Item, Pedido


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoCreateForm

    def form_valid(self, form):
        carrinho = Carrinho(self.request)
        if carrinho:
            pedido = form.save()
            for item in carrinho:
                Item.objects.create(
                    pedido=pedido,
                    produto=item["produto"],
                    preco=item["preco"],
                    quantidade=item["quantidade"],
                )
            carrinho.clear()
            return render(self.request, "pedido/pedido_created.html", {"pedido": pedido})
        return HttpResponseRedirect(reverse("pages:home"))

    """ def lista_pedidos(request):
        queryset = Pedido.objects.all()
        context = {
            'pedidos':queryset
        }
        return render(request, 'pedido/pedidos.html', context) """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carrinho"] = Carrinho(self.request)
        return context

@login_required(login_url='/accounts/login')
def lista_pedidos(request):
        queryset = Pedido.objects.all().order_by('status', 'created')
        context = {
            'pedidos':queryset
        }
        print(queryset)
        return render(request, 'pedido/pedidos.html', context)

def preco_total(preco, quantidade):
    return preco * quantidade

def preco_final(precos):
    preco_final = 0
    for preco in precos:
        preco_final += preco

    return preco_final

@login_required(login_url='/accounts/login')
def detalha_pedido(request, id_pedido):
    nomes = []
    precos = []
    pedido = get_object_or_404(Pedido, id=id_pedido)
    itens = Item.objects.filter(pedido_id=id_pedido)
    for item in itens:
        produto_id = item.produto_id
        nomes.append(Produto.objects.get(produto_id=produto_id))

    for item in itens:
        precos.append(preco_total(item.preco, item.quantidade))

    for nome in nomes:
        print(nome.nome)
    preco_pedido = preco_final(precos)

    context = {
        'pedido':pedido,
        'itens':itens,
        'nomes':nomes,
        'precos':precos,
        'preco_final':preco_pedido,
    }
    return render(request, 'pedido/finalizar_pedido.html', context)

@login_required(login_url='/accounts/login')
def finaliza_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if request.POST:
        form = FinalizaPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.status = True
            pedido.save()
            return redirect('/pedido/lista', {'form':form})

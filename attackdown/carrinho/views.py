from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import override
from django.views.decorators.http import require_POST
from produto.models import Produto

from .carrinho import Carrinho
from .forms import CarrinhoAddProdutoForm

# Create your views here.
def add_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, idProduto=id_produto)

    form = CarrinhoAddProdutoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.add(
            produto = produto,
            quantidade = cd["quantidade"],
            override_quantidade = cd["override"],
        )
    
    return redirect("/carrinho")

def detalha_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, "carrinho\carrinho_detalhado.html", {"carrinho":carrinho})

@require_POST
def remove_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, idProduto=id_produto)
    carrinho.remove(produto)
    
    return redirect("/carrinho")
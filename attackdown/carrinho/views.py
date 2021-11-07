from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import override
from django.views.decorators.http import require_POST
from produto.models import Produto
from django.contrib.auth.decorators import login_required

from .carrinho import Carrinho
from .forms import CarrinhoAddProdutoForm

# Create your views here.
@login_required(login_url='/accounts/login')
def add_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, produto_id=id_produto)

    form = CarrinhoAddProdutoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.add(
            produto = produto,
            quantidade = cd["quantidade"],
            override_quantidade = cd["override"],
        )
    
    return redirect("/carrinho")

@login_required(login_url='/accounts/login')
def detalha_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, "carrinho\carrinho_detalhado.html", {"carrinho":carrinho})

@login_required(login_url='/accounts/login')
@require_POST
def remove_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, produto_id=id_produto)
    carrinho.remove(produto)
    
    return redirect("/carrinho")
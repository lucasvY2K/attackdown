import copy

from django.conf import settings
from .forms import CarrinhoAddProdutoForm
from produto.models import Produto
from decimal import Decimal

class Carrinho:
    def __init__(self, request):
        if request.session.get(settings.CARRINHO_SESSION_ID) is None:
            request.session[settings.CARRINHO_SESSION_ID] = {}

        self.carrinho = request.session[settings.CARRINHO_SESSION_ID]
        self.session = request.session

    def __iter__(self):
        carrinho = copy.deepcopy(self.carrinho)

        produtos = Produto.objects.filter(produto_id__in=carrinho)
        for produto in produtos:
            carrinho[str(produto.produto_id)]["produto"] = produto
        
        for item in carrinho.values():
            item["preco"] = Decimal(item["preco"])
            item["preco_total"] = item["quantidade"] * item["preco"]
            item["update_quantidade_form"] = CarrinhoAddProdutoForm(
                initial = {"quantidade":item["quantidade"], "override":True}
            )

            yield item

    def __len__(self):
        return sum(item["quantidade"] for item in self.carrinho.values())

    def add(self, produto, quantidade=1, override_quantidade=False):
        id_produto = str(produto.produto_id)
        
        if id_produto not in self.carrinho:
            self.carrinho[id_produto] = {
                "quantidade" : 0,
                "preco" : str(produto.preco),
            }

        if override_quantidade:
            self.carrinho[id_produto]["quantidade"] = quantidade
        else:
            self.carrinho[id_produto]["quantidade"] += quantidade

        self.carrinho[id_produto]["quantidade"] = min(20, self.carrinho[id_produto]["quantidade"])
        self.save()

    def remove(self, produto):
        id_produto = str(produto.produto_id)

        if id_produto in self.carrinho:
            del self.carrinho[id_produto]
            self.save()

    def get_preco_total(self):
        return sum(
            Decimal(item["preco"]) * item["quantidade"] for item in self.carrinho.values()
        )

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.CARRINHO_SESSION_ID]
        self.save()
from django.urls import path

from pedido.models import Pedido
from .views import PedidoCreateView
from . import views

app_name = "pedidos"
urlpatterns = [
    path("criar/", PedidoCreateView.as_view(), name="criar"),
    path("lista/", views.lista_pedidos, name="lista"),
    path("detalhar/<str:id_pedido>/", views.detalha_pedido, name="terminar"),
    path("finaliza/<str:id_pedido>/", views.finaliza_pedido, name="finaliza"),
    #path('editar/<str:id_produto>/', views.editar_produto, name="editar-produto")
]
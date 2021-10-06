from django.urls import path
from . import views

urlpatterns = [
    path("", views.detalha_carrinho, name="detalhado"),
    path("add/<int:id_produto>/", views.add_carrinho, name="add-carrinho"),
    path("remove/<int:id_produto>/", views.remove_carrinho, name="remove-carrinho"),
]

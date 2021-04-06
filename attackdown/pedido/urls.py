from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_pedido),
    path('lista/', views.lista_pedidos),
]
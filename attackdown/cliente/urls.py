from django.urls import path
from . import views

urlpatterns =[
    path('cadastrar/', views.novo_cliente),
    path('lista/', views.lista_clientes),
    path('editar/<str:cpf_cliente>/', views.editar_cliente, name="editar-cliente"),
]
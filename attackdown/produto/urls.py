from django.urls import path
from . import views

urlpatterns =[
    path('cadastrar/', views.novo_produto),
    path('lista/', views.lista_produtos),
    path('editar/<str:id_produto>/', views.editar_produto, name="editar-produto")
]
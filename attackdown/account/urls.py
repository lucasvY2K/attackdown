from django.urls import path
from . import views

urlpatterns = [
	path('login', views.login_view, name="entrar"),
	path('register', views.register, name="registrar"),
	path('logout', views.logout_view),
	path('lista_funcionarios', views.exibir_funcionarios),
	path('editar/<str:cpf_funcionario>', views.editar_funcionarios, name="editar-funcionario"),
]
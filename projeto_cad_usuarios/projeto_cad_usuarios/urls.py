
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota. view responsavel, nome de referencia
    # usuarios.com
    #usuarios.com/usuarios
    path('', views.home, name='home'),  # Adicionando o caminho raiz
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]

from django.shortcuts import render
from .models import Usuario
# Create your views here (functions).

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o BD
    novo_usuario = Usuario()
    novo_usuario.nome = nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todosos usuários já cadastrados em uma nova página
    usuarios = {
    'usuarios': Usuario.objects.all()  # Corrigido de object para objects
}
    #Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
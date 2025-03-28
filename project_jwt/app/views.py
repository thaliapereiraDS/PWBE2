# usuarios/views.py
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    cargo = request.data.get('cargo')
    telefone = request.data.get('telefone')
    biografia = request.data.get('biografia')  # Corrigido
    idade = request.data.get('idade')  # Corrigido
    escolaridade = request.data.get('escolaridade')  
    animais = request.data.get('animais')  
    # Verificação de campos obrigatórios
    if not username or not password or not email or not cargo:
        return Response({"Erro": "Informações insuficientes"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificação de usuário e email já existentes
    if Usuario.objects.filter(username=username).exists():
        return Response({"Erro": "Username já existe"}, status=status.HTTP_400_BAD_REQUEST)
    if Usuario.objects.filter(email=email).exists():
        return Response({"Erro": "Email já existente"}, status=status.HTTP_400_BAD_REQUEST)

    
    usuario = Usuario.objects.create_user(  
        username=username,
        password=password,
        email=email,
        cargo=cargo,
        telefone=telefone,
        biografia=biografia,
        idade=idade,
        escolaridade=escolaridade,
        animais=animais 
    )
    return Response({"Mensagem": f"Usuário {username} criado com sucesso"}, status=status.HTTP_201_CREATED)

# View para login de usuário
@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login realizado com sucesso!'}, status=status.HTTP_200_OK)
    return Response({'message': 'Credenciais inválidas!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response ({"Mensagem": "Ola divo"}, status=status.HTTP_200_OK)

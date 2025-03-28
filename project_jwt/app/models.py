from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    biografia = models.TextField(blank=True)
    idade = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length = 30,null = True, blank = True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    escolaridade = models.CharField(max_length=100, blank=True)
    animais = models.IntegerField(default=0)  # Valor padrão
    cargo = models.CharField(max_length=50, blank=True)

from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

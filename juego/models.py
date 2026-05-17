from django.db import models
from django.contrib.auth.models import User


class Matricula(models.Model):
    letras = models.CharField(max_length=3)
    respuesta = models.CharField(max_length=100)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matriculas')

    def __str__(self):
        return f"{self.letras} -> {self.respuesta} ({self.usuario.username})"
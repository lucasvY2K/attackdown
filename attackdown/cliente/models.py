from django.db import models

# Create your models here.
class Cliente(models.Model):
    cpf = models.TextField(unique=True, primary_key=True)
    nome = models.TextField(max_length=45)
    email = models.EmailField(unique=True, max_length=60)
    endereco = models.TextField(max_length= 100)
    telefone = models.TextField(max_length=13)

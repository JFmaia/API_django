from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100),
    rg = models.CharField(max_length=9),
    email = models.EmailField(max_length=100),
    idade = models.IntegerField(),

    def __str__(self):
        return self.nome

    
    

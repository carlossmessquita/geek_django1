from django.db import models


class Aula(models.Model):
    titulo = models.CharField('Nome', max_length=100)
    nota = models.DecimalField('Nota', decimal_places=2, max_digits=4)
    participantes = models.IntegerField('QTD. de Participantes')

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.sobrenome}, {self.nome}'.title()

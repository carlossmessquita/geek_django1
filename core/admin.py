from django.contrib import admin
from .models import Aula, Aluno


class AulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nota', 'participantes')


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Aula, AulaAdmin)
admin.site.register(Aluno, AlunoAdmin)

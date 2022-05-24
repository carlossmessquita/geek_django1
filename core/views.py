from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from core.models import Aula, Aluno


def index(request):
    # print(dir(request))
    aulas = Aula.objects.all()
    alunos = Aluno.objects.all()
    context = {
        'comunidade': 'this.envolve',
        'projeto': 'Amor Pythonico',
        'aulas': aulas,
        'alunos': alunos
    }
    return render(request, 'index.html', context)


def aula(request, pk):
    # classe = Aula.objects.filter(pk=pk).first()
    classe = get_object_or_404(Aula, id=pk)
    context = {
        'aula': classe
    }
    return render(request, 'contato.html', context)


def contato(request):
    return render(request, 'index.html')


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html;  charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

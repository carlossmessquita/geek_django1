from django.shortcuts import render


def index(request):
    context = {
        'comunidade': 'this.envolve',
        'projeto': 'Amor Pythonico'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

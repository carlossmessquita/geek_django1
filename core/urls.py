from django.urls import path
from .views import index, contato, aula

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='index'),
    path('aula/<int:pk>', aula, name='aula')
]

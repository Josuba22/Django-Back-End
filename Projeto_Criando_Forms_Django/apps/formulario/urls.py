from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_celulares, name='lista_celulares'),
    path('celular/<int:celular_id>/', detalhes_celular, name='detalhes_celular'),
    path('cadastrar/', novo_celular, name='novo_celular'),
]

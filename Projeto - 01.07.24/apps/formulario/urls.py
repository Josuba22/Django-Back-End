from django.urls import path
from .views import *

urlpatterns = [
    path('', formulario_lead, name='formulario_lead'),
    path('sucesso/', sucesso, name='sucesso'),
    path('lista_contatos/', lista_contatos, name='lista_contatos')
]

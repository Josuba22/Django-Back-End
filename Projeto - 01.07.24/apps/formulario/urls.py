from django.urls import path
from .views import *

urlpatterns = [
    path('', formulario_lead, name='formulario_lead'),
    path('sucesso/', sucesso, name='sucesso'),
    path('lista-de-leads', VerLeads, name='lista_leads'),
    path('editar-lead/<int:id_lead>/', EditarLead, name='pg_editar_lead')
]

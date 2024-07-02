from django.shortcuts import render, redirect
from .forms import *
from .models import *

def formulario_lead(request):
    if request.method == 'POST':
        form = FormularioLead(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = FormularioLead()
    return render(request, 'index.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')

def VerLeads(request):
    leads_lista = Lead.objects.all()
    return render(request, 'lista_leads.html', {'leads': leads_lista})

def EditarLead(request, id_lead):
    busca_lead = Lead.objects.get(id=id_lead)
    if request.method == 'POST':
        lead_editado = FormularioLead(request.POST, instance=busca_lead)
        if lead_editado.is_valid():
            lead_editado.save()
            return redirect('lista_leads')
    else:
        lead_editado = FormularioLead()
    return render(request, 'lista_leads.html', {'formulario': lead_editado})
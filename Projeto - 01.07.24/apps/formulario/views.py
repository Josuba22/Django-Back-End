from django.shortcuts import render, redirect
from .forms import *
from .models import *

def formulario_lead(request):
    if request.method == 'POST':
        form = FormularioLead(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_contatos')
    else:
        form = FormularioLead()
    return render(request, 'index.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')

def lista_contatos(request):
    leads = Lead.objects.all()
    return render(request, 'lista_contatos.html', {'leads': leads})

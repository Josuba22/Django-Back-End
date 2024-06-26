from django.shortcuts import render, get_object_or_404, redirect
from .models import Celulares
from .forms import CelularForm

def lista_celulares(request):
    celulares = Celulares.objects.all()
    return render(request, 'index.html', {'celulares': celulares})

def detalhes_celular(request):
    celular = get_object_or_404(Celulares, pk=celulares_id)
    return render(request, 'detalhes.html', {'celular': celular})

def novo_celular(request):
    if request.method == "POST":
        form = CelularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_celulares')
    else:
        form = CelularForm()
    return render(request, 'cadastro.html', {'form': form})
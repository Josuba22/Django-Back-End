from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'index.html', context)

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context = {'produto': produto}
    return render(request, 'produto_detalhes.html', context)
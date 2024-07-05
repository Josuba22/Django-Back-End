from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'adicionar_categoria.html', {'form': form})

def ExcluirProduto(request, id_produto):
    busca_produto = Produto.objects.get(id=id_produto)
    if request.method == 'POST':
        busca_produto.delete()
        return redirect('index')
    return render(request, 'conf_excluir_produto.html', {'produto': busca_produto})

def EditarProduto(request, id_produto):
    busca_produto = Produto.objects.get(id=id_produto)
    if request.method == 'POST':
        produto_editado = ProdutoForm(request.POST, instance=busca_produto)
        if produto_editado.is_valid():
            produto_editado.save()
            return redirect('index')
    else:
        produto_editado = ProdutoForm(instance=busca_produto)
    return render(request, 'adicionar_produto.html', {"form": produto_editado})
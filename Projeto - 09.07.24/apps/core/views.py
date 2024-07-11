from django.shortcuts import render, redirect
from .models import *
from .forms import *

def VerIndex(request):
    busca_os = OrdemServico.objects.all()
    
    for os in busca_os:
        valor_os = 0
        for servico in os.servico.all():
            valor_os += servico.valor_servico
        os.valor_total = valor_os

    return render(request, 'index.html', {"ordemservico": busca_os})

def CriarCliente(request):
    busca_clientes = Cliente.objects.all()

    if request.method == 'GET':
        novo_cliente = FormularioCliente()
    else:
        cliente_preenchido = FormularioCliente(request.POST, request. FILES)
        if cliente_preenchido.is_valid():
            cliente_preenchido.save()
        return redirect('pg_inicial')
    return render(request, 'form-cliente.html', {"form_cliente": novo_cliente})

def EditarCliente(request, id_cliente):
    busca_cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'GET':
        editar_cliente = FormularioCliente(instance=busca_cliente)
    else:
        cliente_editado = FormularioCliente(request.POST, instance=busca_cliente)
        if cliente_editado.is_valid():
            cliente_editado.save()
            return redirect('pg_criar_cliente')
        return render(request, 'form-cliente.html', {"form_cliente": editar_cliente})

def CriarEmpresa(request):
    busca_empresas = Empresa.objects.all()

    if request.method == 'GET':
        nova_empresa = FormularioEmpresa()
    else:
        empresa_preenchida = FormularioEmpresa(request.POST)
        if empresa_preenchida.is_valid():
            empresa_preenchida.save()
            return redirect('pg_inicial')
    return render(request, 'form-empresa.html', {"form_empresa": nova_empresa, "empresas": busca_empresas})

def CriarServico(request):
    busca_servicos = Servico.objects.all()

    if request.method == 'GET':
        novo_servico = FormularioServico()
    else:
        servico_preenchido = FormularioServico(request.POST)
        if servico_preenchido.is_valid():
            servico_preenchido.save()
            return redirect('pg_inicial')
    return render(request, 'form-servico.html', {"form_servico": novo_servico, "servicos": busca_servicos})

def CriarCategoria(request):
    busca_categorias = Categoria.objects.all()

    if request.method == 'GET':
        nova_categoria = FormularioCategoria()
    else:
        categoria_preenchida = FormularioCategoria(request.POST)
        if categoria_preenchida.is_valid():
            categoria_preenchida.save()
            return redirect('pg_criar_servico')
    return render(request, 'form-categoria.html', {"form_categoria": nova_categoria, "categorias": busca_categorias})

def CriarOrdemServico(request):

    if request.method == 'GET':
        nova_ordemservico = FormularioEmpresa()
    else:
        ordemservico_preenchido = FormularioEmpresa(request.POST)
        if ordemservico_preenchido.is_valid():
            ordemservico_preenchido.save()
            return redirect('pg_inicial')
    return render(request, 'form-ordemservico.html', {"form_ordemservico": nova_ordemservico})

def EditarEmpresa(request, id_empresa):
    busca_empresa = Cliente.objects.get(id=id_empresa)
    if request.method == 'GET':
        editar_empresa = FormularioCliente(instance=busca_empresa)
    else:
        empresa_editada = FormularioCliente(request.POST, instance=busca_empresa)
        if empresa_editada.is_valid():
            empresa_editada.save()
            return redirect('pg_criar_empresa')
        return render(request, 'form-empresa.html', {"form_empresa": editar_empresa})

def ExcluirCliente(request, id_cliente):
    busca_cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        busca_cliente.delete()
        return redirect('pg_criar_cliente')
    titulo_objeto = busca_cliente.nome
    return render(request, 'conf-excluir.html', {"valor": titulo_objeto})

def ExcluirEmpresa(request, id_empresa):
    busca_empresa = Empresa.objects.get(id=id_empresa)
    if request.method == 'POST':
        busca_empresa.delete()
        return redirect('pg_criar_cliente')
    titulo_objeto = busca_empresa.razao_social
    return render(request, 'conf-excluir.html', {"valor": titulo_objeto})
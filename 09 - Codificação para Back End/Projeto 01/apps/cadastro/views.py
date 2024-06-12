from django.shortcuts import render

def LinkInicial(request):
    return render(request, 'index2.html')

def LinkCadastro(request):
    return render(request, 'cadastro2.html')
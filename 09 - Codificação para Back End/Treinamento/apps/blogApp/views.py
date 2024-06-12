from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return render(request, 'ola_mundo.html')
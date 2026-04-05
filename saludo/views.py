from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):

    contexto = {"nombre":"juancito"}

    return render(request,'saludo/index.html', contexto)

def despedir(request):
    return HttpResponse("<h1>adios Mundo</h1>")

def inicio(request):
    return HttpResponse("<h1>estoy en root</h1>")
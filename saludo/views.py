from django.http import HttpResponse
from django.shortcuts import render


contexto = {
        "nombre":"juancito",
        "esMayor": True,
        "mascotas": ["Firulais", "Bobby", "Bravo"] 
        }


def saludo(request):
    return render(request,'saludo/index.html', contexto)

def despedir(request):
    return render(request,'saludo/despedir.html')

def inicio(request):
    return HttpResponse("<h1>estoy en root</h1>")
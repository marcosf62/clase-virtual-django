from django.http import HttpResponse


def saludo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def despedir(request):
    return HttpResponse("<h1>adios Mundo</h1>")

def inicio(request):
    return HttpResponse("<h1>estoy en root</h1>")
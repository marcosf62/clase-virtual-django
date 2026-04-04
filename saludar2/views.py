from django.http import HttpResponse


def saludar_dos (request):
    return HttpResponse("<p>mini saludo2</p>")
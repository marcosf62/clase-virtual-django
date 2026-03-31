
from django.urls import path, include
from . import views


urlpatterns=[
    path ('saludar/', views.saludo, name="saludo"),
    path ('despedir/', views.despedir, name="despedida"),
    path ('', views.inicio, name="inicio"),
]
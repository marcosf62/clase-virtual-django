
from django.urls import path, include
from . import views


urlpatterns=[
    path ('saludar_dos/', views.saludar_dos, name="saludo"),
]
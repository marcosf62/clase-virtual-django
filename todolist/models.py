from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)
    fecha_completado = models.DateField()
    fecha_creaion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Soy la tarea: {self.nombre}"
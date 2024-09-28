from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10000000, decimal_places=2)
    duracion = models.DurationField() #Formato (HH:MM:SS)
    
    def __str__(self):
        return self.nombre
    
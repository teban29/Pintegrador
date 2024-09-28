from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=100000, decimal_places=2)
    marca = models.ForeignKey('ecomerce.Marca',on_delete=models.SET_NULL,null=True)
    categoria = models.ForeignKey('ecomerce.Categoria', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre
    


class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.

class Cita(models.Model):
    cliente = models.ForeignKey('users.Usuario',on_delete=models.CASCADE,related_name='citas')
    fecha = models.DateTimeField()
    servicio = models.ForeignKey('servicios.Servicio',on_delete=models.CASCADE)
    barbero = models.ForeignKey('users.Usuario',on_delete=models.SET_NULL,null=True,related_name='barbero_citas')
    
    def __str__(self):
        return f"Detalles de la cita:\nCliente: {self.cliente}\nBarbero: {self.barbero}\nServicio: {self.servicio}"
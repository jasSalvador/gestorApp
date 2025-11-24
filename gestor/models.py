from django.db import models
from django.contrib.auth.models import User

#organizacion
class Organizacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    admin_local = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#integrante
class Integrante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    dependiente = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.organizacion.nombre}"
    


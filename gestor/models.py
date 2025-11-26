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
    

#cuota
class Cuota(models.Model):
    meses = [
        ("Enero", "Enero"),
        ("Febrero","Febrero"),
        ("Marzo","Marzo"),
        ("Abril","Abril"),
        ("Mayo","Mayo"),
        ("Junio","Junio"),
        ("Julio","Julio"),
        ("Agosto","Agosto"),
        ("Septiembre","Septiembre"),
        ("Octubre","Octubre"),
        ("Noviembre","Noviembre"),
        ("Diciembre","Diciembre"),
    ]
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE, related_name="cuotas")
    monto = models.DecimalField(max_digits=10, decimal_places=2 )
    fecha_pago = models.DateField()
    mes_pagado = models.CharField(max_length=15, choices=meses)
    anio_pagado = models.PositiveIntegerField()

    def __str__(self):
        return f"Cuota de {self.integrante.user.username} - ${self.monto} ({self.mes_pagado}) {self.anio_pagado}, fecha pago: ({self.fecha_pago})"


#gasto
class Gasto(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

    #sumar todos los items de gastos asociados
    def total(self):
        return sum(item.monto for item in self.items.all())

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"


#item de gasto
class ItemGasto(models.Model):
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE, related_name="items")
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}: ${self.monto}"
    




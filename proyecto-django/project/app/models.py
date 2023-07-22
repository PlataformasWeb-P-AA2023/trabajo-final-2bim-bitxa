from decimal import Decimal
from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return self.nombres


class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    tipo_comida = models.CharField(max_length=100)
    ventas_proyectadas = models.DecimalField(max_digits=10, decimal_places=2)


    @property
    def pago_permiso(self):
        return self.ventas_proyectadas * Decimal('0.8')

    def __str__(self):
        return f"{self.propietario} - {self.direccion}"


class LocalRepuesto(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    valor_mercaderia = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def pago_permiso(self):
        return self.valor_mercaderia * Decimal('0.001')


    def __str__(self):
        return f"{self.propietario} - {self.direccion}"

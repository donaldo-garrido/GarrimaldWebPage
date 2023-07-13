from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Escuela(models.Model):
    nombre_escuela = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_escuela
    
class Tallas(models.Model):
    talla = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(44),
            MinValueValidator(2)
        ]
    )

    def __str__(self):
        return self.talla
    
class Cantidad(models.Model):
    cantidad = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.cantidad

    
class Pedidos(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    chamarra = models.ForeignKey(Tallas, on_delete=models.CASCADE)
    chamarra_largo = models.ForeignKey(Tallas, on_delete=models.CASCADE)
    chamarra_cantidad = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    bordados = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    bordado_nombre = models.CharField(max_length=64)
    celular = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(0)
        ]
    )
    total = models.IntegerField()
    a_cuenta = models.IntegerField()
    resta = models.IntegerField()

    
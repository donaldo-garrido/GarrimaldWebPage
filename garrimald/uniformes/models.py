from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Escuela(models.Model):
    nombre_escuela = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_escuela

class Pedidos(models.Model):

    TALLAS = ((0,'0'), (2,'2'))
    CANTIDAD = ((0,'0'), (1,'1'))

    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=64, default='')

    chamarra = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    #chamarra_largo = models.ForeignKey(Tallas, on_delete=models.CASCADE)
    chamarra_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    #bordados = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    bordado_nombre = models.CharField(max_length=64, default='')
    celular = models.IntegerField(
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(0)
        ]
    )
    total = models.IntegerField()
    a_cuenta = models.IntegerField()
    resta = models.IntegerField()

    
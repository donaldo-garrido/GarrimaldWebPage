from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.

class Escuela(models.Model):
    nombre_escuela = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_escuela

class Pedidos(models.Model):

    TALLAS = ((0,'0'), (2,'2'), (4,'4'), (6,'6'), (8,'8'),
              (10,'10'), (12,'12'), (14,'14'), (16,'16'), 
              (32,'X-CH'), (34,'CH'), (36,'M'), (38,'G'),
              (40,'X-G'), (42,'2X-G'),)
    CANTIDAD = ((0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'))
    
    id = models.AutoField(primary_key=True)

    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=64, default='')

    # Chamarra
    chamarra = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    chamarra_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    chamarra_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    # Playera
    playera = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    playera_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    playera_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    # Pants
    pants = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    pants_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    pants_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    # Sueter hombre
    sueter_hombre = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_hombre_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_hombre_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    # Sueter mujer
    sueter_mujer = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_mujer_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_mujer_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )


    # Camisa
    camisa = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    camisa_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )



    # Blusa
    blusa = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    blusa_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )

    # Pantalón
    pantalon = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    pantalon_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )


    # Jumper
    jumper = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    jumper_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    jumper_cantidad = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )



    bordados = models.IntegerField(
        default=0,
        choices=CANTIDAD,
    )
    bordado_nombre = models.CharField(max_length=64, default='')
    celular = models.IntegerField(
        validators=[
            MaxValueValidator(9999999999),
            MinValueValidator(0)
        ]
    )
    fecha_hora = models.CharField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  max_length=64)


class Precios(models.Model):
    """PRENDAS = (('chamarra','chamarra'), ('playera','playera'), ('pants','pants'), 
               ('sueter','sueter'), ('camisa','camisa'), ('blusa','blusa'),
               ('pantalon','pantalon'), ('jumper', 'jumper'),)"""
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    # Chamarra
    chamarra_cantidad = models.FloatField(default=0,)

    # Playera
    playera_cantidad = models.FloatField(default=0,)

    # Pants
    pants_cantidad = models.FloatField(default=0,)

    # Sueter hombre
    sueter_hombre_cantidad = models.FloatField(default=0,)

    # Sueter mujer
    sueter_mujer_cantidad = models.FloatField(default=0,)

    # Camisa
    camisa_cantidad = models.FloatField(default=0,)

    # Blusa
    blusa_cantidad = models.FloatField(default=0,)

    # Pantalón
    pantalon_cantidad = models.FloatField(default=0,)

    # Jumper
    jumper_cantidad = models.FloatField(default=0,)

    # Bordado
    bordados = models.FloatField(default=0,)



class Total(models.Model):
    pedido = models.IntegerField(default=0, primary_key=True)
    total = models.FloatField(default=0.0)
    a_cuenta = models.FloatField(default=0.0)
    resta = models.FloatField(default=0.0)
    entregado = models.IntegerField(
        default=0,
        choices= ((0,'NO'), (1,'SI')),
    )

"""class Capital(models.Model):
    saldo = models.FloatField(default=0.0)"""

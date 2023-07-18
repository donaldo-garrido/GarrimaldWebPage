from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

    # Sueter
    sueter = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_largo = models.IntegerField(
        default=0,
        choices= TALLAS,
    )
    sueter_cantidad = models.IntegerField(
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

class Pagos(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, default=0)
    total = models.FloatField()
    a_cuenta = models.FloatField()
    resta = models.FloatField()


class Precios(models.Model):
    PRENDAS = (('chamarra','chamarra'), ('playera','playera'), ('pants','pants'), 
               ('sueter','sueter'), ('camisa','camisa'), ('blusa','blusa'),
               ('pantalon','pantalon'), ('jumper', 'jumper'),)
    escuela = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    prenda = models.CharField(max_length=64, default='', choices=PRENDAS)
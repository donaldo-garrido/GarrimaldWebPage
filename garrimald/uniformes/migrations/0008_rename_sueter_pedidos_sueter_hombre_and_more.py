# Generated by Django 4.2.3 on 2023-07-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0007_pagos_pedido_precios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidos',
            old_name='sueter',
            new_name='sueter_hombre',
        ),
        migrations.RenameField(
            model_name='pedidos',
            old_name='sueter_cantidad',
            new_name='sueter_hombre_cantidad',
        ),
        migrations.RenameField(
            model_name='pedidos',
            old_name='sueter_largo',
            new_name='sueter_hombre_largo',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter_mujer',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter_mujer_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter_mujer_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
    ]
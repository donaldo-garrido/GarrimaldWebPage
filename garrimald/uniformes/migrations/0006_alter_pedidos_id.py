# Generated by Django 4.2.3 on 2023-07-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0005_pagos_remove_pedidos_a_cuenta_remove_pedidos_resta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0009_cuenta_resta_total_remove_precios_prenda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='fecha_hora',
            field=models.CharField(default='2023-07-26 22:21:41', max_length=64),
        ),
    ]

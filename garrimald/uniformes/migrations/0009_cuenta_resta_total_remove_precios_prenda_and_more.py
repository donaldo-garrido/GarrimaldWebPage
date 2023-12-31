# Generated by Django 4.2.3 on 2023-07-24 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0008_rename_sueter_pedidos_sueter_hombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField(default=0)),
                ('a_cuenta', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Resta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField(default=0)),
                ('resta', models.FloatField()),
                ('entregado', models.IntegerField(choices=[(0, 'NO'), (1, 'SI')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField(default=0)),
                ('total', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='precios',
            name='prenda',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='fecha_hora',
            field=models.CharField(default='2023-07-24 01:17:17', max_length=64),
        ),
        migrations.AddField(
            model_name='precios',
            name='blusa_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='bordados',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='camisa_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='chamarra_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='jumper_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='pantalon_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='pants_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='playera_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='sueter_hombre_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='precios',
            name='sueter_mujer_cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='precios',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniformes.escuela'),
        ),
        migrations.DeleteModel(
            name='Pagos',
        ),
    ]

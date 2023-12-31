# Generated by Django 4.2.3 on 2023-07-18 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0004_cantidad_title_tallas_chamarra_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('a_cuenta', models.FloatField()),
                ('resta', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='a_cuenta',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='resta',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='total',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='blusa',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='blusa_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='bordados',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='camisa',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='camisa_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='chamarra_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='jumper',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='jumper_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='jumper_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pantalon',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pantalon_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pants',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pants_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pants_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='playera',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='playera_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='playera_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='sueter_largo',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='bordado_nombre',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='celular',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='chamarra',
            field=models.IntegerField(choices=[(0, '0'), (2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12'), (14, '14'), (16, '16'), (32, 'X-CH'), (34, 'CH'), (36, 'M'), (38, 'G'), (40, 'X-G'), (42, '2X-G')], default=0),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='chamarra_cantidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='nombre',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.DeleteModel(
            name='Cantidad',
        ),
        migrations.DeleteModel(
            name='Tallas_chamarra',
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-18 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0006_alter_pedidos_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='pedido',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='uniformes.pedidos'),
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenda', models.CharField(choices=[('chamarra', 'chamarra'), ('playera', 'playera'), ('pants', 'pants'), ('sueter', 'sueter'), ('camisa', 'camisa'), ('blusa', 'blusa'), ('pantalon', 'pantalon'), ('jumper', 'jumper')], default='', max_length=64)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniformes.pedidos')),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioABC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=200)),
                ('Familia', models.TextField()),
                ('Cantidad', models.CharField(max_length=200)),
                ('Costo', models.CharField(max_length=200)),
                ('Precio', models.CharField(max_length=200)),
                ('Volumen', models.CharField(max_length=200)),
            ],
        ),
    ]

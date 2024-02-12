# Generated by Django 5.0.1 on 2024-02-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_alter_inventarioabc_costo_alter_inventarioabc_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=200)),
                ('Cantidad', models.CharField(max_length=200)),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Fecha', models.DateField()),
            ],
        ),
    ]

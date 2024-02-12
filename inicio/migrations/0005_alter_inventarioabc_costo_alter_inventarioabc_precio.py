# Generated by Django 5.0.1 on 2024-02-05 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_inventarioabc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarioabc',
            name='Costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='inventarioabc',
            name='Precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

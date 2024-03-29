# Generated by Django 5.0.1 on 2024-01-28 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.area')),
            ],
        ),
        migrations.DeleteModel(
            name='Proyect',
        ),
    ]

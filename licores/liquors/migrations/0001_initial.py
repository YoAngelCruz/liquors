# Generated by Django 3.1.3 on 2023-03-27 20:19

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liquor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destilado', models.CharField(blank=True, default='alcohol', max_length=50)),
                ('nombre', models.CharField(blank=True, default='???', max_length=50)),
                ('description', models.TextField(blank=True, default='Licor')),
                ('pais_origen', models.CharField(blank=True, default='Mexico', max_length=50)),
                ('size', models.CharField(blank=True, default='1L', max_length=50)),
                ('tipo_envase', models.CharField(blank=True, default='Botella de cristal', max_length=50)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('caducidad', models.DateField(default=datetime.datetime(2023, 6, 27, 14, 19, 55, 150330))),
                ('edicion', models.CharField(default='Standar', max_length=50)),
                ('precio', models.FloatField(default=1000)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2023-02-24 19:53

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
                ('destilado', models.CharField(default='alcohol', max_length=50)),
                ('nombre', models.CharField(default='???', max_length=50)),
                ('description', models.TextField(default='Licor')),
                ('size', models.CharField(default='1L', max_length=50)),
                ('tipo_envase', models.CharField(default='Botella de cristal', max_length=50)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('caducidad', models.DateField(default=datetime.datetime(2023, 5, 24, 13, 53, 54, 891702))),
                ('edicion', models.CharField(default='Standar', max_length=50)),
                ('precio', models.FloatField(default=1000)),
            ],
        ),
    ]
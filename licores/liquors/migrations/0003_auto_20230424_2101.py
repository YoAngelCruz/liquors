# Generated by Django 3.1.3 on 2023-04-25 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquors', '0002_auto_20230413_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquor',
            name='caducidad',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 21, 1, 7, 816867)),
        ),
    ]
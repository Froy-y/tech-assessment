# Generated by Django 3.2.7 on 2021-11-11 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20211111_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 11, 16, 52, 48, 476490)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 16, 52, 48, 476490)),
        ),
    ]

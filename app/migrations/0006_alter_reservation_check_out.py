# Generated by Django 3.2.7 on 2021-11-11 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211110_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 1, 23, 28, 575607)),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-11 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20211111_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 11, 16, 53, 15, 73852)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 16, 53, 15, 73852)),
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-11 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211111_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='amenities',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 12, 11, 46, 54, 519547)),
        ),
    ]
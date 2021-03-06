# Generated by Django 3.2.7 on 2021-11-11 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='listing',
            field=models.ManyToManyField(to='app.Listing'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 11, 21, 3, 19, 920037)),
        ),
    ]

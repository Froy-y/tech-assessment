# Generated by Django 3.2.7 on 2021-11-10 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('check_in', models.DateField(verbose_name='Check-In')),
                ('check_out', models.DateField(verbose_name='Check-Out')),
            ],
        ),
    ]
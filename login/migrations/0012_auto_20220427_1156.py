# Generated by Django 3.1.2 on 2022-04-27 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20220427_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_details',
            name='BookingUser',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='coname',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='fromdestination',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='todestination',
            field=models.CharField(max_length=15),
        ),
    ]

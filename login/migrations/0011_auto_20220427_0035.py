# Generated by Django 3.1.2 on 2022-04-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20220426_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_details',
            name='TicketNumber',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]

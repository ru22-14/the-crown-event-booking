# Generated by Django 3.2.20 on 2023-07-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbooking', '0017_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 3.2.20 on 2023-07-21 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventbooking', '0009_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 7, 21, 9, 22, 49, 376293, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=80),
        ),
    ]
# Generated by Django 3.2.20 on 2023-07-25 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventbooking', '0014_alter_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='timeblock',
            field=models.IntegerField(choices=[(1, '08:00 AM - 12:00 PM'), (2, '14:00 PM - 18:00 PM'), (3, '20:00 PM - 00:00 AM')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_bookings', to='eventbooking.event'),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-23 18:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_directorate_facility_reservation_delete_slot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='day',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

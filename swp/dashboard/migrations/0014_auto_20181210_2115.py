# Generated by Django 2.1.2 on 2018-12-10 15:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_merge_20181210_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 15, 45, 51, 6159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 15, 45, 51, 7159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messannouncements',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 15, 45, 51, 7159, tzinfo=utc)),
        ),
    ]
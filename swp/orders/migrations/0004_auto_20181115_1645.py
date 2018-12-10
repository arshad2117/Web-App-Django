# Generated by Django 2.1.2 on 2018-11-15 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181115_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 826559, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='manualorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 827103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 828909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 15, 16, 45, 45, 827948, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.0.1 on 2021-01-04 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 4, 4, 23, 24, 124436)),
        ),
        migrations.AlterField(
            model_name='consumption',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
    ]
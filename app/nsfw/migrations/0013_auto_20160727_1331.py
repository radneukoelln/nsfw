# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsfw', '0012_station_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='data',
            new_name='pm10_data',
        ),
    ]

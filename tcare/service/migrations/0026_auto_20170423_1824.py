# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0025_auto_20170423_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentdetail',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='physiotherapist',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]

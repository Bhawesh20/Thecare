# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20170328_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('', '--choose--'), ('M', 'Male'), ('F', 'Female')], default='', max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0037_auto_20170426_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
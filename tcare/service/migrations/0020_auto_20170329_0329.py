# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 21:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_types', to=settings.AUTH_USER_MODEL),
        ),
    ]
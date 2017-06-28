# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20170327_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtestdata',
            name='address',
            field=models.CharField(default=123, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointmentdetail',
            name='service_required',
            field=models.CharField(choices=[('', ''), ('MALE NURSE', 'Male Nurse'), ('FEMALE NURSE', 'Female Nurse'), ('BABY SITTER', 'Babysitter')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='prescriptiondata',
            name='address',
            field=models.CharField(max_length=1000),
        ),
    ]

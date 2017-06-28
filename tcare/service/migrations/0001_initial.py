# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default=None, max_length=10)),
                ('service_required', models.CharField(choices=[('MN', 'Male Nurse'), ('FN', 'Female Nurse'), ('BS', 'Babysitter'), ('PT', 'physiotherapist')], default='MN', max_length=2)),
                ('served_by', models.CharField(default='Unassigned', max_length=50)),
                ('appointment_date', models.DateField()),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
    ]
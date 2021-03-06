# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_auto_20170326_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabtestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('test_type', models.CharField(choices=[('--Lab Test--', ''), ('Complete Blood Count', 'Complete Blood Count'), ('Fast Blood Sugar', 'Fast Blood Sugar'), ('Postprandial Blood Sugar', 'Postprandial Blood Sugar'), ('Lipid Profile', 'Lipid Profile'), ('Uric Acid', 'Uric Acid'), ('Blood Pressure Test', 'Blood Pressure Test'), ('--Vaccination--', ''), ('H1N1', 'H1N1'), ('Chicken Pox', 'Chicken Pox'), ('Typhoid', 'Typhoid'), ('Hepatitis B', 'Hepatitis B'), ('Pneumonia', 'Pneumonia')], default=' ', max_length=30)),
                ('test_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Booked', 'Booked')], default='Pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Physiotherapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default=None, max_length=10)),
                ('served_by', models.CharField(default='Unassigned', max_length=50)),
                ('appointment_date', models.DateField()),
                ('period', models.CharField(choices=[('', ''), ('1day', '1day'), ('7day', '7days'), ('15day', '15days'), ('30day', '30days')], default='', max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Booked', 'Booked')], default='Pending', max_length=50)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='address',
            field=models.CharField(default=123, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='duration',
            field=models.CharField(choices=[('', ''), ('8hrs', '8hrs/day'), ('12hrs', '12hrs/day'), ('16hrs', '16hrs/day'), ('24hrs', '24hrs/day')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='appointmentdetail',
            name='period',
            field=models.CharField(choices=[('', ''), ('1day', '1day'), ('7day', '7days'), ('15day', '15days'), ('30day', '30days')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='prescriptiondata',
            name='address',
            field=models.CharField(default='Null', max_length=1000),
        ),
        migrations.AlterField(
            model_name='appointmentdetail',
            name='service_required',
            field=models.CharField(choices=[('', ''), ('MALENURSE', 'Male Nurse'), ('FEMALENURSE', 'Female Nurse'), ('BABYSITTER', 'Babysitter')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedata',
            name='duration',
            field=models.CharField(choices=[('', ''), ('8hrs', '8hrs/day'), ('12hrs', '12hrs/day'), ('16hrs', '16hrs/day'), ('24hrs', '24hrs/day')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedata',
            name='period',
            field=models.CharField(choices=[('', ''), ('7day', '7days'), ('15day', '15days'), ('30day', '30days')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedata',
            name='service_required',
            field=models.CharField(choices=[('MN', 'Male Nurse'), ('FN', 'Female Nurse'), ('BS', 'Babysitter')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='packagedata',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Booked', 'Booked')], default='Pending', max_length=50),
        ),
    ]

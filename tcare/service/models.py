from django.db import models
from django.core.validators import *
# Create your models here.
from django.contrib.auth.models import User
from .choices import service_choices,gender_choices, user_type_choices, status_choices, duration_choice, period_choice, test_choices, servicetype_choice
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	gender =models.CharField(max_length=10, choices=gender_choices, default = '')
	profile_photo = models.ImageField()
	contact_number = models.CharField(max_length=10,default= None)
	age = models.PositiveIntegerField()
	address = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.pk) + ' ' +self.user.username

class UserType(models.Model):
	user = models.OneToOneField(User,related_name='user_types')
	user_type = models.CharField(max_length=20, choices = user_type_choices, default = 'Patient')
	def __str__(self):
		return str(self.pk) + ' ' +self.user.username

class AppointmentDetail(models.Model):
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10,default= None)
	service_required = models.CharField(max_length=20, choices = service_choices, default = '')
	served_by = models.CharField(max_length=50, default='Unassigned')
	appointment_date = models.DateField(auto_now=False, auto_now_add=False)
	duration = models.PositiveIntegerField(default=13, help_text='value 2 to 24', validators=[MaxValueValidator(24),
            MinValueValidator(2)])
	period = models.PositiveIntegerField(default=16, help_text='value 1 to 30', validators=[MaxValueValidator(30),
            MinValueValidator(1)])
	status = models.CharField(max_length=50, choices =status_choices, default='Pending')
	address = models.CharField(max_length=1000)

	def __str__(self):
		return str(self.pk) +'. Patient: ' + self.patient_name +' -->Service:' + self.service_required

class PrescriptionData(models.Model):
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	prescribed_by = models.CharField(max_length=50)
	prescription_date = models.DateField(auto_now=False, auto_now_add=False) ##update timestamp
	prescription_image = models.ImageField()
	address = models.CharField(max_length=1000)
	buy = models.BooleanField(default=False)
	def __str__(self):
		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Prescribed_by: ' + self.prescribed_by

class PhysiotherapistDetail(models.Model):
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10,default= None)
	served_by = models.CharField(max_length=50, default='Unassigned')
	appointment_date = models.DateField(auto_now=False, auto_now_add=False)
	period = models.PositiveIntegerField(default=16, help_text='value 1 to 30', validators=[MaxValueValidator(30),
            MinValueValidator(1)])
	status = models.CharField(max_length=50, choices =status_choices, default='Pending')
	address = models.CharField(max_length=1000)

class LabtestData(models.Model):
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=10,default= None)
	test_type = models.CharField(max_length=30, choices=test_choices, default = '')
	test_date = models.DateField(auto_now=False, auto_now_add=False)
	status = models.CharField(max_length=50, choices=status_choices ,default='Pending')
	address = models.CharField(max_length=1000)


	def __str__(self):
		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Test type: ' + self.test_type

class PackageData(models.Model):
	user = models.ForeignKey(User, default=1)
	user = models.ForeignKey(User, default=1)
	patient_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10,default= None)
	service_required = models.CharField(max_length=20, choices = servicetype_choice, default = ' ')
	duration = models.CharField(max_length=20, choices = duration_choice, default = ' ')
	period = models.CharField(max_length=20, choices = period_choice, default = ' ')
	status = models.CharField(max_length=50,choices=status_choices, default='Pending')
	def __str__(self):
		return str(self.pk)+ '. Patient: ' + self.patient_name + '  Prescribed_by: ' + self.service_required


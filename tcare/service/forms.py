from django import forms
from django.contrib.auth.models import Permission, User
from .models import AppointmentDetail,PhysiotherapistDetail, PrescriptionData, PackageData, UserProfile, LabtestData
from django.contrib.auth.forms import UserCreationForm



class AppointmentForm(forms.ModelForm):

	class Meta:
		model = AppointmentDetail
		fields = ['patient_name', 'phone_number', 'service_required','appointment_date','duration','period','address']
		widgets = {
			'appointment_date': forms.DateInput(attrs={'class': 'datetime-input'}),
			'address': forms.Textarea,
		}

class UsersignupForm(forms.ModelForm):
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)
	password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput)
	password2 = forms.CharField(label=("Password confirmation"),widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))

	class Meta:
		model = User
		fields = ['username','email']

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('The two password fields did not match.')
		return password2

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if User.objects.filter(email=email).exclude(username=username).exists():
			raise forms.ValidationError("This email is already used")
		return email

	def save(self,commit = True):   
		user = super(UsersignupForm, self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class PhysiotherapistForm(forms.ModelForm):

	class Meta:
		model = PhysiotherapistDetail
		fields = ['patient_name', 'phone_number','appointment_date','period','address']
		widgets = {
			'appointment_date': forms.DateInput(attrs={'class': 'datetime-input'}),
			'address': forms.Textarea,
		}

class PrescriptionForm(forms.ModelForm):

	class Meta:
		model = PrescriptionData
		fields = ['patient_name', 'prescribed_by', 'prescription_date','address', 'prescription_image' ]
		widgets = {
			'prescription_date': forms.DateInput(attrs={'class': 'datetime-input2'}),
			'address': forms.Textarea,
		}

class LabtestForm(forms.ModelForm):
	class Meta:
		model = LabtestData
		fields = ['patient_name', 'contact_number', 'test_type', 'test_date', 'address']
		widgets = {
			'test_date': forms.DateInput(attrs={'class': 'datetime-input'}),
			'address': forms.Textarea,
		}

class PackageForm(forms.ModelForm):
	class Meta:
		model = PackageData
		fields = ['patient_name', 'phone_number', 'service_required', 'duration', 'period']

class UserprofileForm(forms.ModelForm):
	profile_photo = forms.ImageField(required = False)
	class Meta:
		model = UserProfile
		fields = ['gender', 'contact_number', 'age', 'address','profile_photo']
		widgets = {
			'address': forms.Textarea,
		}
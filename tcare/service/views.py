from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import AppointmentDetail,PhysiotherapistDetail, PrescriptionData, PackageData, UserProfile, LabtestData, UserType
from django.template import loader
from .forms import AppointmentForm,UsersignupForm,PhysiotherapistForm, PrescriptionForm, PackageForm, UserprofileForm, LabtestForm
from django.http import HttpResponse
# Create your views here.

def home(request):
	if not request.user.is_authenticated():
		return render(request, 'service/home_visitor.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request, 'service/index.html', {'userdata' : userdata,})

def register(request):
	form = UsersignupForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password2']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				usertypedata, created=UserType.objects.get_or_create(user=user)
				userdata = UserProfile.objects.filter(user = request.user)
				return render(request, 'service/index.html', {'userdata' : userdata,})
	context = {
	"form": form,
	}
	return render(request, 'service/register.html', context)


def login_user(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					usertypedata, created=UserType.objects.get_or_create(user=user)
					userdata = UserProfile.objects.filter(user = request.user)
					return render(request, 'service/index.html', {'userdata' : userdata,})
				else:
					return render(request, 'service/login.html', {'error_message': 'Your account has been disabled'})
			else:
				return render(request, 'service/login.html', {'error_message': 'Invalid login'})
		return render(request, 'service/login.html')
	else:
		usertypedata, created=UserType.objects.get_or_create(user=request.user)
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request, 'service/index.html', {'userdata' : userdata,})


def logout_user(request):
	logout(request)
	return render(request, 'service/login.html')

#about Appointments
def add_appointment(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			appointment1 = form.save(commit=False)
			appointment1.user = request.user
			appointment1.save()
			all_appointment = AppointmentDetail.objects.filter(user = request.user).order_by('-pk')
			return render(request,'service/appointment.html', {'all_appointment' : all_appointment, 'userdata' : userdata,})
		return render(request, 'service/add_appointment.html', {'form': form,  'userdata' : userdata,})

def appointment(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_appointment = AppointmentDetail.objects.filter(user = request.user).order_by('-pk')
		return render(request,'service/appointment.html', {'all_appointment' : all_appointment, 'userdata' : userdata,})

def view_appointment(request,appointment_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		appointment1 = AppointmentDetail.objects.filter(pk=appointment_id, user=request.user).order_by('-pk')
		return render(request,'service/appointment_view.html', {'appointment1' : appointment1, 'userdata' : userdata,})

def del_appointment(request, appointment_id=None):
	appointment1 = AppointmentDetail.objects.get(pk=appointment_id)
	appointment1.delete()
	userdata = UserProfile.objects.filter(user = request.user)
	all_appointment = AppointmentDetail.objects.filter(user = request.user).order_by('-pk')
	return render(request,'service/appointment.html', {'all_appointment' : all_appointment, 'userdata' : userdata,})




#About Physiotherapist
def add_physiotherapist(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = PhysiotherapistForm(request.POST or None)
		if form.is_valid():
			physiotherapist1 = form.save(commit=False)
			physiotherapist1.user = request.user
			physiotherapist1.save()
			all_physiotherapist = PhysiotherapistDetail.objects.filter(user = request.user).order_by('-pk')
			return render(request,'service/physiotherapist.html', {'all_physiotherapist' : all_physiotherapist, 'userdata' : userdata,})
		return render(request, 'service/add_physiotherapist.html', {'form': form,  'userdata' : userdata,})

def physiotherapist(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_physiotherapist = PhysiotherapistDetail.objects.filter(user = request.user).order_by('-pk')
		return render(request,'service/physiotherapist.html', {'all_physiotherapist' : all_physiotherapist, 'userdata' : userdata,})

def view_physiotherapist(request,physiotherapist_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		physiotherapist1 = PhysiotherapistDetail.objects.filter(pk=physiotherapist_id, user=request.user).order_by('-pk')
		return render(request,'service/physiotherapist_view.html', {'physiotherapist1' : physiotherapist1, 'userdata' : userdata,})

def del_physiotherapist(request, physiotherapist_id=None):
	physiotherapist1 = PhysiotherapistDetail.objects.get(pk=physiotherapist_id)
	physiotherapist1.delete()
	userdata = UserProfile.objects.filter(user = request.user)
	all_physiotherapist = PhysiotherapistDetail.objects.filter(user = request.user).order_by('-pk')
	return render(request,'service/physiotherapist.html', {'all_physiotherapist' : all_physiotherapist, 'userdata' : userdata,})



#About Prescriptions
def add_prescription(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = PrescriptionForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			prescription1 = form.save(commit=False)
			prescription1.user = request.user
			prescription1.save()
			all_prescriptions = PrescriptionData.objects.filter(user = request.user).order_by('-pk')
			return render(request,'service/prescription.html', {'all_prescriptions' : all_prescriptions,'userdata' : userdata,})
		return render(request, 'service/add_prescription.html', {'form': form, 'userdata' : userdata,})

def prescription(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_prescriptions = PrescriptionData.objects.filter(user = request.user).order_by('-pk')
		return render(request,'service/prescription.html', {'all_prescriptions' : all_prescriptions, 'userdata' : userdata,})

def del_prescription(request, prescription_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		prescription1 = PrescriptionData.objects.get(pk=prescription_id)
		if not prescription1.buy:
			prescription1.delete()
		userdata = UserProfile.objects.filter(user = request.user)
		all_prescriptions = PrescriptionData.objects.filter(user = request.user).order_by('-pk')
		return render(request,'service/prescription.html', {'all_prescriptions' : all_prescriptions, 'userdata' : userdata,})

def buy_medicine(request, prescription_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		prescription1 = PrescriptionData.objects.get(pk=prescription_id)
		prescription1.buy = True
		prescription1.save()
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request,'service/buy_prescription.html', {'userdata' : userdata,})
#About Physiotherapist


#About Lab test
def add_test(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = LabtestForm(request.POST or None)
		if form.is_valid():
			test1 = form.save(commit=False)
			test1.user = request.user
			test1.save()
			all_test = LabtestData.objects.filter(user = request.user).order_by('-pk')
			return render(request,'service/lab_test.html', {'all_test' : all_test, 'userdata' : userdata,})
		return render(request, 'service/add_labtest.html', {'form': form,  'userdata' : userdata,})

def lab_test(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else: 
		userdata = UserProfile.objects.filter(user = request.user)
		all_test = LabtestData.objects.filter(user = request.user).order_by('-pk')
		return render(request,'service/lab_test.html', {'all_test' : all_test, 'userdata' : userdata,})

def view_lab_test(request,test_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		labtest1 = LabtestData.objects.filter(pk=test_id, user=request.user).order_by('-pk')
		return render(request,'service/lab_test_view.html', {'labtest1' : labtest1, 'userdata' : userdata,})

def del_lab_test(request, test_id=None):
	labtest1 = LabtestData.objects.get(pk=test_id)
	labtest1.delete()
	userdata = UserProfile.objects.filter(user = request.user)
	all_test = LabtestData.objects.filter(user = request.user).order_by('-pk')
	return render(request,'service/lab_test.html', {'all_test' : all_test, 'userdata' : userdata,})



#About Package
def package(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		all_packages = PackageData.objects.filter(user = request.user)
		return render(request,'service/package.html', {'all_packages' : all_packages, 'userdata' : userdata,})

def add_package(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		form = PackageForm(request.POST or None)
		if form.is_valid():
			package1 = form.save(commit=False)
			package1.user = request.user
			package1.save()
			all_packages = PackageData.objects.filter(user = request.user)
			return render(request,'service/package.html', {'all_packages' : all_packages, 'userdata' : userdata,})
		return render(request, 'service/add_package.html', {'form': form, 'userdata' : userdata,})




def user_detail(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user = request.user)
		return render(request,'service/user.html', {'userdata' : userdata,})

def edit_user(request, id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		userdata = UserProfile.objects.filter(user__id=id) #filter is used because if no userdata it will return empty list
		#import ipdb;ipdb.set_trace()
		if userdata :  # If Data is in database
			form = UserprofileForm(request.POST or None, request.FILES or None, instance = userdata[0])
			#import ipdb;ipdb.set_trace()
			if form.is_valid():
				#import ipdb;ipdb.set_trace()
				pkt1 = form.save(commit=False)
				pkt1.user = request.user
				pkt1.save()
				userd = UserProfile.objects.filter(user__id=id)
				return render(request,'service/user.html', {'userdata' : userd,})
			return render(request,'service/useredit.html', {'form' : form, 'userdata' : userdata,})
		else: #If no data in databse
			form = UserprofileForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				pkt1 = form.save(commit=False)
				pkt1.user = request.user
				pkt1.save()
				userd = UserProfile.objects.filter(user = request.user)
				return render(request,'service/user.html', {'userdata' : userd,})
			userdata = UserProfile.objects.filter(user = request.user)
			return render(request,'service/useredit.html', {'form' : form, 'userdata' : userdata,})

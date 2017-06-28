from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.template import loader
from service.models import PrescriptionData, UserType
from django.http import HttpResponse
# Create your views here.
def admin_prescription(request):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		if request.user.user_types.user_type=='Staff':
			all_prescriptions = PrescriptionData.objects.filter(buy=True)
			return render(request,'./office/admin_prescription.html', {'all_prescriptions' : all_prescriptions,})
		else:
			return HttpResponse(status=404)

def allow_buy(request, prescription_id=None):
	if not request.user.is_authenticated():
		return render(request, 'service/login.html')
	else:
		if request.user.user_types.user_type=='Staff':
			prescription1 = PrescriptionData.objects.get(pk=prescription_id)
			prescription1.buy = False
			prescription1.save()
			all_prescriptions = PrescriptionData.objects.filter(buy=True)
			return render(request,'./office/admin_prescription.html', {'all_prescriptions' : all_prescriptions,})
		else:
			return HttpResponse(status=404)
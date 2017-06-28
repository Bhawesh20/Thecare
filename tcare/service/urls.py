from django.conf.urls import url
from . import views

app_name = 'service'

urlpatterns = [
	url(r'^$', views.home, name='index'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^register/$', views.register, name='register'),
	url(r'^home/$', views.home, name='home'),


	url(r'^appointment/$', views.appointment, name='appointment'),
	url(r'^add_appointment/$', views.add_appointment, name='add_appointment'),
	url(r'^appointment/(?P<appointment_id>\d+)$', views.view_appointment, name = 'view_appointment'),
	url(r'^delete_appointment/(?P<appointment_id>\d+)$', views.del_appointment, name = 'del_appointment'),

	url(r'^physiotherapist/$', views.physiotherapist, name='physiotherapist'),
	url(r'^add_physiotherapist_appointment/$', views.add_physiotherapist, name='add_physiotherapist'),
	url(r'^physiotherapist/(?P<physiotherapist_id>\d+)$', views.view_physiotherapist, name = 'view_physiotherapist'),
	url(r'^delete_physiotherapist_appointment/(?P<physiotherapist_id>\d+)$', views.del_physiotherapist, name = 'del_physiotherapist'),


	url(r'^prescription/$', views.prescription, name='prescription'),
	url(r'^add_prescription/$', views.add_prescription, name='add_prescription'),
	url(r'^delete_prescription/(?P<prescription_id>\d+)$', views.del_prescription, name = 'del_prescription'),
	url(r'^buy_medicine/(?P<prescription_id>\d+)/$', views.buy_medicine, name = 'buy_medicine'),


	url(r'^package/$', views.package, name='package'),
	url(r'^add_package/$', views.add_package, name='add_package'),

	
	url(r'^lab_test/$', views.lab_test, name = 'lab_test'),
	url(r'^add_lab_test/$', views.add_test, name = 'add_test'),
	url(r'^view_lab_test/(?P<test_id>\d+)$', views.view_lab_test, name = 'view_lab_test'),
	url(r'^delete_lab_test/(?P<test_id>\d+)$', views.del_lab_test, name = 'del_lab_test'),

	url(r'^user/$', views.user_detail, name = 'user_detail'),
	url(r'^edit_user/(?P<id>\d+)/$', views.edit_user, name = 'edit_user'),
	

	url(r'^logout/$', views.logout_user, name='logout_user'),
]
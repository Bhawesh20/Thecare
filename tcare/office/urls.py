from django.conf.urls import url
from . import views
app_name = 'office'

urlpatterns = [
	url(r'^prescriptions/$', views.admin_prescription, name='admin_prescription'),
	url(r'^allow_buy_medicine/(?P<prescription_id>\d+)/$', views.allow_buy, name = 'allow_buy'),
]
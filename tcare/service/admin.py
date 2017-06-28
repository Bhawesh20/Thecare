from django.contrib import admin
from .models import AppointmentDetail,PhysiotherapistDetail, PrescriptionData, PackageData, UserProfile, LabtestData, UserType
# Register your models here.
admin.site.register(AppointmentDetail)
admin.site.register(PhysiotherapistDetail)
admin.site.register(UserType)
admin.site.register(PrescriptionData)
admin.site.register(LabtestData)
admin.site.register(PackageData)
admin.site.register(UserProfile)


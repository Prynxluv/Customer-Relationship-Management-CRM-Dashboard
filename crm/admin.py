
from django.contrib import admin
from . models import Customer, Information, SkinCareInquiry, SkinCareReport, BookAppointment, ScheduleAppointment, Treatment, TreatmentList, Report

# Register your models here.


admin.site.register(Customer),
admin.site.register(Information),
admin.site.register(SkinCareInquiry),
admin.site.register(SkinCareReport),
admin.site.register(BookAppointment),
admin.site.register(ScheduleAppointment),
admin.site.register(Treatment),
admin.site.register(TreatmentList),
admin.site.register(Report),




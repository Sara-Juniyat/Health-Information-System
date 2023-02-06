
from django.contrib import admin
from .models import *


class AddressAdmin(admin.ModelAdmin):
    Model = Address
    list_display = ('streetNb', 'bldngName', 'AptFloor', 'city')


admin.site.register(Address, AddressAdmin)


class NurseAdmin(admin.ModelAdmin):
    list_display = ('salary', 'created')


admin.site.register(Nurse, NurseAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'salary', 'created')


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'weight', 'height', 'allergies')


admin.site.register(Patient, PatientAdmin)


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'doctor', 'observation')


admin.site.register(Consultation, ConsultationAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ('fee', 'payment_state', 'consultation')


admin.site.register(Bill, BillAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('consultation', 'consultation')


admin.site.register(Prescription, PrescriptionAdmin)

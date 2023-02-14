from django import forms
from .models import *


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = "__all__"


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"

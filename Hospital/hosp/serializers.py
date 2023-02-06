from rest_framework import serializers
from .models import *


class serializerDoctor(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['email', 'salary', 'created']


class serializerPatient(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['email', 'weight', 'height', 'allergies']


# Doctor, Patient, Document, Appointment, Consultation, Bill, Prescription, Nurse


class serializerAddress(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['streetNb', 'bldngName', 'AptFloor', 'city']


class serializerDocument(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['title', 'type', 'image', 'patient', 'doctor', 'observation']


class serializerNurse(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nurse
        fields = ['salary', 'created']


class serializerAppointment(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['day', 'start_time', 'end_time', 'patient', 'state', 'consulted']


class serializerConsultation(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consultation
        fields = ['appointment', 'doctor', 'observation']


class serializerBill(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['fee', 'payment_state', 'consultation']


class serializerPrescription(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = ['treatment', 'consultation']

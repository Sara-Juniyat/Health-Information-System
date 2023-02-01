# Create your views here.


from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import *
from .forms import *


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializerDoctor
    permission_class = [IsAuthenticated]

def Doctor_API(request):
    context = {}
    # create object of form
    form = DoctorForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Doctor-API", context)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializerPatient
    permission_class = [IsAuthenticated]


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = serializerPatient
    permission_class = [IsAuthenticated]

import os

from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from rest_framework import viewsets, generics, status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponsePermanentRedirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from xhtml2pdf import pisa

import hosp
from hosp.forms import *
from hosp.models import *
from hosp.serializers import *
from rest_framework.response import Response
from io import BytesIO


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializerDoctor
    permission_class = [IsAuthenticated]


def doctor_api(request):
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


def patient_api(request):
    context = {}
    # create object of form
    form = PatientForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Patient-API", context)


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = serializerPatient
    permission_class = [IsAuthenticated]


def nurse_api(request):
    context = {}
    # create object of form
    form = NurseForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Nurse-API", context)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = serializerAppointment
    permission_class = [IsAuthenticated]


def appointment_api(request):
    context = {}
    # create object of form
    form = AppointmentForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Appointment-API", context)


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = serializerBill
    permission_class = [IsAuthenticated]


def bill_api(request):
    context = {}
    # create object of form
    form = BillForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Bill-API", context)


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = serializerConsultation
    permission_class = [IsAuthenticated]


def consultation_api(request):
    context = {}
    # create object of form
    form = ConsultationForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Consultation-API", context)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = serializerAddress
    permission_class = [IsAuthenticated]


def address_api(request):
    context = {}
    # create object of form
    form = AddressForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Address-API", context)


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = serializerPrescription
    permission_class = [IsAuthenticated]


def prescription_api(request):
    context = {}
    # create object of form
    form = PrescriptionForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Prescription-API", context)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = serializerDocument
    permission_class = [IsAuthenticated]


def document_api(request):
    context = {}
    # create object of form
    form = DocumentForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context['form'] = form
    return render(request, "Document-API", context)


def pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error generating PDF: %s' % pdf.err, status=400)


def bill_pdf(request):
    bill_response = Bill.objects.filter(payment_state="Pending", consultation__appointment__patient=request.GET.get("id")).values(
        'fee',
        'payment_state',
        'consultation__doctor__first_name',
        'consultation__doctor__last_name',
        'consultation__appointment__patient__first_name',
        'consultation__appointment__patient__last_name',
        'consultation__observation'
    )
    return pdf('bill_template.html', {'responses': bill_response})


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(UpdateAPIView):
    """
        An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProfileView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#
#     def get_object(self):
#         print(self.request.user)
#         return self.request.user


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # this will check if it is authenticated or not
    authentication_classes = [JWTAuthentication]  # this will handel authentication automatically

    def get_object(self):
        print(self.request.user)
        return self.request.user


class UpdateProfileView(generics.UpdateAPIView):
    """
        An endpoint for updating password.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

# Create your views here.


from django.shortcuts import render
from rest_framework import viewsets

import hosp
from .serializers import *
from .forms import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializerDoctor


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


def display(request):
    data = hosp.objects.all()
    context = {
                'response': data,
        }
    return render(request, "temp2.html", context)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    @staticmethod
    def get(request, *args, **kwargs):
        data = hosp.objects.all()
        context = {
            'responses': data
        }
        pdf = render_to_pdf('pdf_template.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    @staticmethod
    def get(request, *args, **kwargs):
        data = hosp.objects.all()
        context = {
            'responses': data
        }
        pdf = render_to_pdf('pdf_template.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "hospital%s.pdf" % "12341231"
        content = "attachment; filename='%s'" % filename
        response['Content-Disposition'] = content
        return response

"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from hosp.views import *

router = routers.DefaultRouter()
router.register(r'Doctor', DoctorViewSet)
router.register(r'Patient', PatientViewSet)
router.register(r'Nurse', NurseViewSet)
router.register(r'Bill', BillViewSet)
router.register(r'Appointment', AppointmentViewSet)
router.register(r'Address', AddressViewSet)
router.register(r'Prescription', PrescriptionViewSet)
router.register(r'Document', DocumentViewSet)
router.register(r'Consultation', ConsultationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Doctor-API/', include(router.urls)),
    path('Patient-API/', include(router.urls)),
    path('Nurse-API/', include(router.urls)),
    path('Appointment-API/', include(router.urls)),
    path('Bill-API/', include(router.urls)),
    path('Consultation-API/', include(router.urls)),
    path('Address-API/', include(router.urls)),
    path('prescription', include(router.urls)),
    path('Document', include(router.urls)),
    path('pdfview/', ViewPDF.as_view(), name="pdf_view"),
    path('pdfdownload/', DownloadPDF.as_view(), name="pdf_download"),

    path('signup', RegisterUserAPIView.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('profile-get', ProfileView.as_view(), name='profile'),
    path('change-password', ChangePasswordView.as_view(), name='change_password'),
    path('update-profile/<int:pk>', UpdateProfileView.as_view(), name='auth_update_profile'),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # /login/ /logout/
    path('refreshToken', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifyToken', TokenVerifyView.as_view(), name='verify_token'),
]

from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User


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


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance
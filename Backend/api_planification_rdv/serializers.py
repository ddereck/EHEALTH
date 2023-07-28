from rest_framework import serializers
from .models import Appointment, Actor, Patient, Availability

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'specialty']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email']

class AppointmentSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    patient = PatientSerializer()

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

    class Meta:
        model = Appointment
        fields = ['id', 'actor', 'patient', 'date', 'start_time', 'end_time']

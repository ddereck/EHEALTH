from rest_framework import generics, filters
from .serializers import PatientSerializer, ActorSerializer, AppointmentSerializer, MedicalRecordSerializer
from .models import Patient, Actor, Appointment, MedicalRecord

class PatientSearchView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'age', 'sex', 'medical_history']

class ActorSearchView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'specialty']

class AppointmentSearchView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'time', 'actor__first_name', 'actor__last_name', 'patient__first_name', 'patient__last_name']


class MedicalRecordSearchView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__first_name', 'patient__last_name', 'consultation_date', 'diagnosis', 'treatment']

class PatientUpdateView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class ActorUpdateView(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class AppointmentUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordUpdateView(generics.UpdateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

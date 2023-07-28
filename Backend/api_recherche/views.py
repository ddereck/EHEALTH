from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient, Actor, Appointment, MedicalRecord
from .serializers import PatientSerializer, ActorSerializer, AppointmentSerializer, MedicalRecordSerializer
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class SearchView(APIView):
    def get(self, request, format=None):
        return Response({
            'patients': reverse('patient-search', request=request, format=format),
            'actors': reverse('actor-search', request=request, format=format),
            'appointments': reverse('appointment-search', request=request, format=format),
            'medical-records': reverse('medical-record-search', request=request, format=format),
        })

class PatientSearchView(APIView):
    def get(self, request, format=None):
        # Récupérer les critères de recherche depuis les paramètres de requête
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        age = request.GET.get('age')
        patient_number = request.GET.get('patient_number')

        # Effectuer la recherche des patients en utilisant les critères fournis
        patients = Patient.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name, age=age, patient_number=patient_number)

        # Serializer les résultats de recherche des patients
        serialized_patients = PatientSerializer(patients, many=True)

        return Response(serialized_patients.data)

class ActorSearchView(APIView):
    def get(self, request, format=None):
        # Récupérer les critères de recherche depuis les paramètres de requête
        nom = request.GET.get('nom')
        specialite = request.GET.get('specialite')
        # ... autres critères de recherche spécifiques aux médecins

        # Effectuer la recherche des médecins en utilisant les critères fournis
        actors = Actor.objects.filter(nom__icontains=nom, specialite__nom__icontains=specialite)
        # ... autre logique de recherche spécifique aux médecins

        # Serializer les résultats de recherche des médecins
        serialized_actors = ActorSerializer(actors, many=True)

        return Response(serialized_actors.data)

class AppointmentSearchView(APIView):
    def get(self, request, format=None):
        # Récupérer les critères de recherche depuis les paramètres de requête
        actor_id = request.GET.get('actor')
        patient_id = request.GET.get('patient')
        date = request.GET.get('date')
        # ... autres critères de recherche spécifiques aux rendez-vous

        # Effectuer la recherche des rendez-vous en utilisant les critères fournis
        appointments = Appointment.objects.filter(actor_id=actor_id, patient_id=patient_id, date=date)
        # ... autre logique de recherche spécifique aux rendez-vous

        # Serializer les résultats de recherche des rendez-vous
        serialized_appointments = AppointmentSerializer(appointments, many=True)

        return Response(serialized_appointments.data)

class MedicalRecordSearchView(APIView):
    permission_classes = [IsAuthenticated]  # Exige une authentification pour accéder à la vue

    def get(self, request, format=None):
        # Récupérer les critères de recherche depuis les paramètres de requête
        patient_id = request.GET.get('patient_id')
        diagnosis = request.GET.get('diagnosis')
        # ... autres critères de recherche spécifiques aux dossiers médicaux

        # Effectuer la recherche des dossiers médicaux en utilisant les critères fournis
        medical_records = MedicalRecord.objects.filter(patient_id=patient_id, diagnosis__icontains=diagnosis)
        # ... autre logique de recherche spécifique aux dossiers médicaux

        # Serializer les résultats de recherche des dossiers médicaux
        serialized_medical_records = MedicalRecordSerializer(medical_records, many=True)

        return Response(serialized_medical_records.data)

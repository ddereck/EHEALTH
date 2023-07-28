from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment
from .models import Actor
from api_gestion_medecins.models import Availability
from .serializers import AvailabilitySerializer, ActorSerializer, AppointmentSerializer
from rest_framework import status
#from .utils import send_email_reminder, send_notification_reminder


class ActorAvailabilityView(APIView):
    def get(self, request):
        # Logique pour consulter les disponibilités des médecins
        availabilities = Actor.objects.all()  # Exemple de récupération des disponibilités des médecins depuis la base de données
        serialized_availabilities = AvailabilitySerializer(availabilities, many=True)  # Exemple de sérialisation des disponibilités
        return Response(serialized_availabilities.data)

class ActorSelectionView(APIView):
    def get(self, request):
        # Logique pour sélectionner un médecin pour le rendez-vous
        doctors = Actor.objects.filter(specialty='Cardiologie')  # Exemple de récupération des médecins avec une spécialité spécifique
        serialized_doctors =ActorSerializer(doctors, many=True)  # Exemple de sérialisation des médecins
        return Response(serialized_doctors.data)

class AppointmentCreateView(APIView):
    def post(self, request):
        # Logique pour créer un nouveau rendez-vous
        serializer = AppointmentSerializer(data=request.data)  # Exemple d'utilisation d'un sérialiseur pour valider les données du rendez-vous
        if serializer.is_valid():
            appointment = serializer.save()  # Exemple de sauvegarde du rendez-vous dans la base de données
            return Response("Rendez-vous créé avec succès")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentRetrieveUpdateDeleteView(APIView):
    def get(self, request, appointment_id):
        # Logique pour récupérer les informations sur un rendez-vous
        try:
            appointment = Appointment.objects.get(id=appointment_id)  # Exemple de récupération du rendez-vous depuis la base de données
            serialized_appointment = AppointmentSerializer(appointment)  # Exemple de sérialisation du rendez-vous
            return Response(serialized_appointment.data)
        except Appointment.DoesNotExist:
            return Response("Rendez-vous introuvable", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, appointment_id):
        # Logique pour mettre à jour un rendez-vous
        try:
            appointment = Appointment.objects.get(id=appointment_id)  # Exemple de récupération du rendez-vous depuis la base de données
            serializer = AppointmentSerializer(appointment, data=request.data)  # Exemple d'utilisation d'un sérialiseur pour mettre à jour les données du rendez-vous
            if serializer.is_valid():
                updated_appointment = serializer.save()  # Exemple de sauvegarde du rendez-vous mis à jour dans la base de données
                return Response("Rendez-vous mis à jour avec succès")
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Appointment.DoesNotExist:
            return Response("Rendez-vous introuvable", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, appointment_id):
        # Logique pour supprimer un rendez-vous
        try:
            appointment = Appointment.objects.get(id=appointment_id)  # Exemple de récupération du rendez-vous depuis la base de données
            appointment.delete()  # Exemple de suppression du rendez-vous de la base de données
            return Response("Rendez-vous supprimé avec succès")
        except Appointment.DoesNotExist:
            return Response("Rendez-vous introuvable", status=status.HTTP_404_NOT_FOUND)



class AppointmentReminderView(APIView):
    def post(self, request):
        # Logique pour envoyer les rappels de rendez-vous aux patients

        # # 1. Récupérer les rendez-vous à rappeler
        # appointments = Appointment.objects.filter(date__gte=datetime.date.today())  # Exemple de récupération des rendez-vous à partir d'aujourd'hui

        # # 2. Envoyer les rappels pour chaque rendez-vous
        # for appointment in appointments:
        #     # Envoyer un e-mail de rappel
        #     send_email_reminder(appointment.patient.email, "Rappel de rendez-vous", f"Votre rendez-vous est prévu le {appointment.date}. N'oubliez pas !")

        #     # Envoyer une notification sur le backoffice du patient
        #     send_notification_reminder(appointment.patient, "Rappel de rendez-vous", f"Votre rendez-vous est prévu le {appointment.date}. N'oubliez pas !")

        # 3. Retourner une réponse
        return Response("Rappels de rendez-vous envoyés avec succès")


class AppointmentHistoryView(APIView):
    def get(self, request):
        # Logique pour consulter l'historique des rendez-vous du patient
        appointments = Appointment.objects.filter(patient=request.user)  # Exemple de récupération des rendez-vous du patient connecté
        serialized_appointments = AppointmentSerializer(appointments, many=True)  # Exemple de sérialisation des rendez-vous
        return Response(serialized_appointments.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HospitalizationSerializer
from .permissions import IsActor, IsAdmin

class HospitalizationCreateView(APIView):
    permission_classes = [IsActor]  # Exige que l'utilisateur soit un médecin pour accéder à cette vue

    def post(self, request):
        serializer = HospitalizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HospitalizationDetailView(APIView):
    permission_classes = [IsActor, IsAdmin]  # Exige que l'utilisateur soit un médecin ou un administrateur pour accéder à cette vue

    def get(self, request, hospitalization_id):
        # Logique pour récupérer les informations sur une hospitalisation spécifique
        return Response("Informations sur l'hospitalisation récupérées avec succès")

    def put(self, request, hospitalization_id):
        # Logique pour mettre à jour une hospitalisation spécifique
        return Response("Hospitalisation mise à jour avec succès")

    def delete(self, request, hospitalization_id):
        # Logique pour supprimer une hospitalisation spécifique
        return Response("Hospitalisation supprimée avec succès")

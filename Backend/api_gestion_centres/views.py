from Backend.api_auth.models import User
from rest_framework import generics
from .models import Centre, Abonnement, Profil, Profil_Affectation
from .serializers import CentreSerializer, AbonnementSerializer, ProfilSerializer, ProfilAffectationSerializer

class CentreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer


class CentreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer


class AbonnementListAPIView(generics.ListAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer

class ProfilListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer


class ProfilRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer


class ProfilAffectationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profil_Affectation.objects.all()
    serializer_class = ProfilAffectationSerializer

class ProfilAffectationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profil_Affectation.objects.all()
    serializer_class = ProfilAffectationSerializer
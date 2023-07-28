from rest_framework import generics
from .models import Actor, Specialty, Availability
from .serializers import ActorSerializer, SpecialtySerializer, AvailabilitySerializer

class ActorCreateView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'id'

class ActorSearchView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # Logique pour la recherche des médecins

class SpecialtyManagementView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    lookup_field = 'id'

class AvailabilityManagementView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    lookup_field = 'id'

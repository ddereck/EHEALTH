from rest_framework import generics
from .serializers import CentreSerializer
from .models import Centre


#pour les opérations de liste/création dun centre
class CentreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

#de récupération/mise à jour/suppression dun centre
class CentreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

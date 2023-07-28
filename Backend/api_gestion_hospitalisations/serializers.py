from rest_framework import serializers
from .models import Hospitalization

class HospitalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalization
        fields = '__all__'

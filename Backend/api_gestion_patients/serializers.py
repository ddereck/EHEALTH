from rest_framework import serializers
from .models import Patient
from Backend.api_auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'telephone', 'email']

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Utilisez PrimaryKeyRelatedField pour récupérer l'utilisateur existant

    class Meta:
        model = Patient
        fields = ['user', 'date_of_birth', 'patient_number', 'groupe_sanguin']

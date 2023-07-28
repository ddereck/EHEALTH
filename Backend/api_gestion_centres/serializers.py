from rest_framework import serializers
from .models import Centre, Abonnement, Profil, Profil_Affectation
from Backend.api_auth.models import User

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'

class CentreSerializer(serializers.ModelSerializer):
    abonnements = AbonnementSerializer(many=True, read_only=True)

    class Meta:
        model = Centre
        fields = '__all__'

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'

class ProfilAffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil_Affectation
        fields = '__all__'

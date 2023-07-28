from django.db import models
from Backend.api_auth.models import User

class Actor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialite = models.ForeignKey('Specialty', on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100)
    # Autres champs pour les informations sur le médecin

class Specialty(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    # Autres champs pour les informations sur les spécialités médicales

class Availability(models.Model):
    medecin = models.ForeignKey('Actor', on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    # Autres champs pour les informations sur les disponibilités des médecins



    # Cardiologie : Spécialité médicale dédiée aux maladies du cœur et des vaisseaux sanguins.
    # Neurologie : S'occupe des maladies et des troubles du système nerveux, y compris le cerveau et la moelle épinière.
    # Pédiatrie : Spécialisée dans les soins de santé des enfants, des nouveau-nés aux adolescents.
    # Dermatologie : Traite les maladies de la peau, des ongles et des cheveux.
    # Chirurgie générale : Impliquée dans une variété de procédures chirurgicales, souvent sur les organes abdominaux.
    # Gynécologie : Se concentre sur la santé reproductive des femmes et les problèmes liés à l'appareil reproducteur féminin.
    # Ophtalmologie : Traite les maladies et les troubles de l'œil et des structures oculaires.
    # Orthopédie : Spécialité des troubles musculo-squelettiques, des os, des articulations et des muscles.
    # Oto-rhino-laryngologie (ORL) : Concerne les maladies de l'oreille, du nez et de la gorge.
    # Radiologie : Utilise les techniques d'imagerie pour diagnostiquer et traiter les maladies et les blessures internes.
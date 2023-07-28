from django.db import models

class Hospitalization(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=100)
    actor = models.ForeignKey('Actor', on_delete=models.SET_NULL, null=True)
    # Autres champs liés à l'admission

class Diagnosis(models.Model):
    hospitalization = models.ForeignKey('Hospitalization', on_delete=models.CASCADE)
    description = models.TextField()
    # Autres champs liés au diagnostic

class Treatment(models.Model):
    hospitalization = models.ForeignKey('Hospitalization', on_delete=models.CASCADE)
    description = models.TextField()
    # Autres champs liés au traitement

class HealthStatus(models.Model):
    hospitalization = models.ForeignKey('Hospitalization', on_delete=models.CASCADE)
    observation = models.TextField()
    date = models.DateTimeField()
    # Autres champs liés au suivi de l'état de santé

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    # Autres champs liés aux coordonnées du patient

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    # Autres champs liés au médecin

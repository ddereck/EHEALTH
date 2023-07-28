from django.db import models
from Backend.api_gestion_hospitalisations.models import Patient

    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    taille = models.CharField(max_length=200)
    tension_arterielle = models.CharField(max_length=200)
    poids = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    electrophorese = models.CharField(max_length=200)
    antecedents_medicaux = models.CharField(max_length=200)
    allergies = models.CharField(max_length=200)
    isDiabetic = models.BooleanField(default=False)
    isAsthmatic = models.BooleanField(default=False)
    isTensionnaire = models.BooleanField(default=False)
    diagnosis = models.ForeignKey('Diagnosis', on_delete=models.CASCADE)
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)
    treatment = models.ForeignKey('Treatment', on_delete=models.CASCADE)
    # ... autres champs  ...

    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création du dossier médical
    dernier_rdv = models.DateTimeField(null=True, blank=True)  # Date du dernier rendez-vous
    prochain_rdv = models.DateTimeField(null=True, blank=True)  # Date du prochain rendez-vous prévu
    medicaments_en_cours = models.TextField(blank=True)  # Liste des médicaments en cours pour le patient
    resultat_examens = models.TextField(blank=True)  # Résultats d'examens médicaux
    notes_medicales = models.TextField(blank=True)  # Notes médicales générales
    recommandations = models.TextField(blank=True)  # Recommandations pour le patient
    autres_informations = models.TextField(blank=True) 
    
    def __str__(self):
        return f"Medical Record for {self.patient}"
    

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis_text = models.TextField()

    def __str__(self):
        return f"Diagnosis on {self.date} for {self.patient}"



class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"Consultation on {self.date} for {self.patient}"


class Treatment(models.Model): 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=200)
    exam_requests = models.CharField(max_length=200)
    exam_results = models.CharField(max_length=200)

    def __str__(self):
        return f"Treatment: for {self.patient}"
   


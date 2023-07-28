from django.db import models
from django.utils import timezone
from Backend.api_gestion_medecins.models import Actor, Availability
from Backend.api_gestion_patients.models import Patient

class Appointment(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.actor} on {self.date}"

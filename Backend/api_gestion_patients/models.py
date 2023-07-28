from django.db import models
from django.utils import timezone
from datetime import date
from Backend.api_auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    date_of_birth = models.DateField()
    patient_number = models.CharField(max_length=100) #géré par le système
    groupe_sanguin = models.CharField(max_length=10)

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

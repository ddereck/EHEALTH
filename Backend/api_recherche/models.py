from django.db import models

class Patient(models.Model):
    # ...

    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(email__icontains=query) |
            models.Q(phone_number__icontains=query) |
            models.Q(address__icontains=query)
        )

class Actor(models.Model):
    # ...

    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query) |
            models.Q(specialty__icontains=query) |
            models.Q(availability__icontains=query) |
            models.Q(working_hours__icontains=query)
        )

class Appointment(models.Model):
    # ...

    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(patient__first_name__icontains=query) |
            models.Q(patient__last_name__icontains=query) |
            models.Q(actor__first_name__icontains=query) |
            models.Q(actor__last_name__icontains=query) |
            models.Q(date__icontains=query) |
            models.Q(time__icontains=query)
        )

class MedicalRecord(models.Model):
    # ...

    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            models.Q(patient__first_name__icontains=query) |
            models.Q(patient__last_name__icontains=query) |
            models.Q(actor__first_name__icontains=query) |
            models.Q(actor__last_name__icontains=query) |
            models.Q(consultation_date__icontains=query) |
            models.Q(diagnosis__icontains=query) |
            models.Q(treatment__icontains=query) |
            models.Q(prescription__icontains=query) |
            models.Q(results__icontains=query)
        )

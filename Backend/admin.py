from django.contrib import admin
from Backend.models import *
from Backend.api_auth.models import User
from Backend.api_gestion_centres.models import Centre, Abonnement, Profil, Profil_Affectation
from Backend.api_gestion_medecins.models import Actor, Specialty, Availability
from Backend.api_gestion_patients.models import Patient
from Backend.api_gestion_dossiers_medicaux.models import Consultation, Diagnosis, Treatment, MedicalRecord
from Backend.api_recherche.models import Actor, Appointment, MedicalRecord, Patient






# Register your models here.
admin.site.register(User)
admin.site.register(Profil)
admin.site.register(Centre)
admin.site.register(Abonnement)
admin.site.register(Profil_Affectation)
admin.site.register(Specialty)
admin.site.register(Availability)
admin.site.register(Consultation)
admin.site.register(Diagnosis)
admin.site.register(Treatment)
admin.site.register(Actor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Patient)


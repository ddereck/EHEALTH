from django.db import models

class Invoice(models.Model):
    numero_facture = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_facture = models.DateField()
    # Autres champs pour les informations de la facture

class Payment(models.Model):
    mode_paiement = models.CharField(max_length=100)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    # Autres champs pour les informations de paiement

class InsuranceReimbursement(models.Model):
    compagnie_assurance = models.CharField(max_length=100)
    montant_remboursement = models.DecimalField(max_digits=10, decimal_places=2)
    date_remboursement = models.DateField()
    # Autres champs pour les informations de remboursement d'assurance

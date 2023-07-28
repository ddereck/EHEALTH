from rest_framework import serializers
from .models import Invoice, Payment, InsuranceReimbursement

class InvoiceSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Invoice

    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Payment

    class Meta:
        model = Payment
        fields = '__all__'

class InsuranceReimbursementSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle InsuranceReimbursement

    class Meta:
        model = InsuranceReimbursement
        fields = '__all__'

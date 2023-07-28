from rest_framework import generics
from .models import Invoice, Payment, InsuranceReimbursement
from .serializers import InvoiceSerializer, PaymentSerializer, InsuranceReimbursementSerializer

class InvoiceCreateView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class InsuranceReimbursementCreateView(generics.CreateAPIView):
    queryset = InsuranceReimbursement.objects.all()
    serializer_class = InsuranceReimbursementSerializer

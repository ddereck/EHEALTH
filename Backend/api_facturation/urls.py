from django.urls import path
from .views import (
    InvoiceCreateView, InvoiceRetrieveUpdateDeleteView,
    PaymentCreateView, InsuranceReimbursementCreateView
)

urlpatterns = [
    path('invoices/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDeleteView.as_view(), name='invoice-detail'),
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
    path('insurance-reimbursements/', InsuranceReimbursementCreateView.as_view(), name='insurance-reimbursement-create'),
]

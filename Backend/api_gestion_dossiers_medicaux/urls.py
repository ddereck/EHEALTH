from django.urls import path
from .views import (
    MedicalRecordListCreateView, MedicalRecordDetailView,
    ConsultationListCreateView, ConsultationDetailView,
    DiagnosisListCreateView, DiagnosisDetailView,
    TreatmentListCreateView, TreatmentDetailView,
)

urlpatterns = [
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('consultations/', ConsultationListCreateView.as_view(), name='consultation-list-create'),
    path('consultations/<int:pk>/', ConsultationDetailView.as_view(), name='consultation-detail'),
    path('diagnoses/', DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('diagnoses/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis-detail'),
    path('treatments/', TreatmentListCreateView.as_view(), name='treatment-list-create'),
    path('treatments/<int:pk>/', TreatmentDetailView.as_view(), name='treatment-detail'),
]

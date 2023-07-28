from django.urls import path, reverse
from .views import SearchView, PatientSearchView, ActorSearchView, AppointmentSearchView, MedicalRecordSearchView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('search/patients/', PatientSearchView.as_view(), name='patient-search'),
    path('search/actors/', ActorSearchView.as_view(), name='actor-search'),
    path('search/appointments/', AppointmentSearchView.as_view(), name='appointment-search'),
    path('search/medical-records/', MedicalRecordSearchView.as_view(), name='medical-record-search'),
]

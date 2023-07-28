from django.urls import path
from .views import HospitalizationCreateView

urlpatterns = [
    path('hospitalizations/', HospitalizationCreateView.as_view(), name='hospitalization-create'),
    # Autres URL pour les autres vues
]

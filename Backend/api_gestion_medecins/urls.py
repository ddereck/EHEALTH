from django.urls import path
from .views import (
    ActorCreateView,
    ActorRetrieveUpdateDeleteView,
    ActorSearchView,
    SpecialtyManagementView,
    AvailabilityManagementView,
)

urlpatterns = [
    path('actors/', ActorCreateView.as_view(), name='actor-create'),
    path('actors/<int:id>/', ActorRetrieveUpdateDeleteView.as_view(), name='actor-detail'),
    path('actors/search/', ActorSearchView.as_view(), name='actor-search'),
    path('specialties/', SpecialtyManagementView.as_view(), name='specialty-management'),
    path('availability/', AvailabilityManagementView.as_view(), name='availability-management'),
]

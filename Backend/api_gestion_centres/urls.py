from django.urls import path
from . import views

app_name = 'api_gestion_centres'

urlpatterns = [
    path('centres/', views.CentreListCreateAPIView.as_view(), name='centre-list-create'),
    path('centres/<int:pk>/', views.CentreRetrieveUpdateDestroyAPIView.as_view(), name='centre-retrieve-update-destroy'),
    path('centres/<int:pk>/abonnements/', views.AbonnementListAPIView.as_view(), name='centre-abonnements-list'),
    path('profils/', views.ProfilListCreateAPIView.as_view(), name='profil-list-create'),
    path('profils/<int:pk>/', views.ProfilRetrieveUpdateDestroyAPIView.as_view(), name='profil-retrieve-update-destroy'),
    path('affectations/', views.ProfilAffectationListCreateAPIView.as_view(), name='profil-affectation-list-create'),
    path('affectations/<int:pk>/', views.ProfilAffectationRetrieveUpdateDestroyAPIView.as_view(), name='profil-affectation-retrieve-update-destroy'),
]

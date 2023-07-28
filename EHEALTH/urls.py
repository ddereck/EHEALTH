"""
URL configuration for EHEALTH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Backend.api_generation_rapports.views import HomePageView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomePageView.as_view(), name='home'),
    path('Backend/api_gestion_centres/', include('Backend.api_gestion_centres.urls')),
    path('Backend/api_auth/', include('Backend.api_auth.urls')),
    path('Backend/api_facturation/', include('Backend.api_facturation.urls')),
    path('Backend/api_generation_rapports/', include('Backend.api_generation_rapports.urls')),
    path('Backend/api_gestion_dossiers_medicaux/', include('Backend.api_gestion_dossiers_medicaux.urls')),
    path('Backend/api_gestion_hospitalisations/', include('Backend.api_gestion_hospitalisations.urls')),
    path('Backend/api_gestion_medecins/', include('Backend.api_gestion_medecins.urls')),
    path('Backend/api_gestion_patients/', include('Backend.api_gestion_patients.urls')),
    path('Backend/api_messagerie/', include('Backend.api_messagerie.urls')),
    path('Backend/api_planification_rdv/', include('Backend.api_planification_rdv.urls')),
    path('Backend/api_recherche/', include('Backend.api_recherche.urls')),
]

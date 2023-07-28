from django.urls import include, path

urlpatterns = [
    path('api/', include('api_gestion_dossiers_medicaux.urls')),
]

from django.urls import path
from django.views.generic.base import TemplateView
from .api import (
    ReportGenerationView,
    DataAnalysisView,
    PerformanceReportView,
    PatientReportView,
    ReportExportView,
    ScheduledReportGenerationView,
)

# Définir les URL des vues de l'API
urlpatterns = [
    # URL pour générer un rapport personnalisé
    path('reports/generate/', ReportGenerationView.as_view(), name='report-generation'),
    
    # URL pour effectuer une analyse de données
    path('data/analysis/', DataAnalysisView.as_view(), name='data-analysis'),
    
    # URL pour générer un rapport sur les performances
    path('reports/performance/', PerformanceReportView.as_view(), name='performance-report'),
    
    # URL pour générer un rapport sur les patients
    path('reports/patients/', PatientReportView.as_view(), name='patient-report'),
    
    # URL pour exporter un rapport
    path('reports/export/', ReportExportView.as_view(), name='report-export'),
    
    # URL pour planifier la génération automatique de rapports
    path('reports/schedule/', ScheduledReportGenerationView.as_view(), name='schedule-report-generation'),
]
class HomePageView(TemplateView):
    template_name = 'Backend/home.html'

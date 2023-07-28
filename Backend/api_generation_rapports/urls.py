from django.urls import path
from . import views

app_name = 'api_generation_rapports'

urlpatterns = [
    # URL pour générer un rapport personnalisé
    path('reports/generate/', views.ReportGenerationView.as_view(), name='report-generation'),
    
    # URL pour effectuer une analyse de données
    path('data/analysis/', views.DataAnalysisView.as_view(), name='data-analysis'),
    
    # URL pour générer un rapport sur les performances
    path('reports/performance/', views.PerformanceReportView.as_view(), name='performance-report'),
    
    # URL pour générer un rapport sur les patients
    path('reports/patients/', views.PatientReportView.as_view(), name='patient-report'),
    
    # URL pour exporter un rapport
    path('reports/export/', views.ReportExportView.as_view(), name='report-export'),
    
    # URL pour planifier la génération automatique de rapports
    path('reports/schedule/', views.ScheduledReportGenerationView.as_view(), name='schedule-report-generation'),
]

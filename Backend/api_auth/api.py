from django.urls import path, include

urlpatterns = [
    path('auth/', include('api_auth.urls')),
]

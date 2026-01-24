from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing, name='main'),  # Using testing view as the main page
    path('testing/', views.testing, name='testing'),  # Keeping this for backward compatibility
]
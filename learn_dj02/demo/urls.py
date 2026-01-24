from django.urls import path
from . import views 

urlpatterns = [
    path('subject/', views.subjectStudy, name='subject-study'),
]
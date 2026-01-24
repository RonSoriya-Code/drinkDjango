from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:student_id>/', views.StudentDetailView.as_view(), name='student-detail'),
]
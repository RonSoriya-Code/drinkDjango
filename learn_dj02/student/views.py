from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse("<h1>Welcome to Student Management System</h1>")

class StudentListView(View):
    def get(self, request):
        return HttpResponse("<h1>Student List</h1><p>List of students will be shown here.</p>")

class StudentDetailView(View):
    def get(self, request, student_id):
        return HttpResponse(f"<h1>Student Details</h1><p>Details for student ID: {student_id}</p>")
from django.shortcuts import render
from django.http import HttpResponse

def my_app(request):
    return HttpResponse("Hello world!")

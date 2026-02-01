from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm
from django.contrib.auth.views import LoginView


# Create your views here.

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'authen/register.html'
    success_url = reverse_lazy('authen:login')
    success_message = 'Account created successfully'

class UserLoginView(LoginView):
    template_name = 'authen/login.html'  # Use this template
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, UserLoginView  # <--- Import your custom view here

app_name = 'authen'

urlpatterns = [
    # CORRECT: Use UserLoginView.as_view() without arguments
    path('login/', UserLoginView.as_view(), name='login'),
    
    path('register/', RegisterView.as_view(), name='register'),
    
    path('logout/', LogoutView.as_view(next_page='authen:login'), name='logout'),
]
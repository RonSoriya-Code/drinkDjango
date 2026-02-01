from django.urls import path

from .views import SaleCreateView, SaleDeleteView, SaleDetailView, SaleListView, SaleUpdateView

app_name = 'sale'

urlpatterns = [
    path('', SaleListView.as_view(), name='sale_list'),
    path('add/', SaleCreateView.as_view(), name='sale_add'),
    path('<int:pk>/', SaleDetailView.as_view(), name='sale_detail'),
    path('<int:pk>/edit/', SaleUpdateView.as_view(), name='sale_edit'),
    path('<int:pk>/delete/', SaleDeleteView.as_view(), name='sale_delete'),
    
]
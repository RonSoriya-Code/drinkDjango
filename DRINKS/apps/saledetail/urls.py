from django.urls import path

from .views import SaleDetailCreateView, SaleDetailDeleteView, SaleDetailDetailView, SaleDetailListView, SaleDetailUpdateView

app_name = 'saledetail'

urlpatterns = [
    path('', SaleDetailListView.as_view(), name='saledetail_list'),
    path('add/', SaleDetailCreateView.as_view(), name='saledetail_add'),
    path('<int:pk>/', SaleDetailDetailView.as_view(), name='saledetail_detail'),
    path('<int:pk>/edit/', SaleDetailUpdateView.as_view(), name='saledetail_edit'),
    path('<int:pk>/delete/', SaleDetailDeleteView.as_view(), name='saledetail_delete'),
    
]
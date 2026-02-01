"""
URL configuration for DRINKS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('apps.category.urls', namespace='list_category')),
    path('customer/', include('apps.customer.urls', namespace='list_customer')),
    path('', include('apps.dashboard.urls', namespace='dashboard')),
    path('product/', include('apps.product.urls', namespace='list_product')),
    path('sale/', include('apps.sale.urls', namespace='list_sale')),
    path('saledetail/', include('apps.saledetail.urls', namespace='list_saledetail')),
    # path('supplier/', include('apps.supplier.urls', namespace='list_supplier')),
    path('authen/', include('apps.authen.urls', namespace='authen')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.product.forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/list_product.html'
    context_object_name = 'products'



class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('list_product:product_list')
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/edit_product.html'
    success_url = reverse_lazy('list_product:product_list')
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('list_product:product_list')
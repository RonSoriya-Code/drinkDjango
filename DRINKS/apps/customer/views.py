from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import CustomerForm

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list_customer.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/add_customer.html'
    success_url = reverse_lazy('customer:customer_list') 

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/detail_customer.html'
    context_object_name = 'customer'

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/edit_customer.html'
    success_url = reverse_lazy('customer:customer_list') 

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('customer:customer_list') 


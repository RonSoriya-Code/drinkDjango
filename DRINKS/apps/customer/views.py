from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import CustomerForm, CustomerProfileForm

from .models import Customer, CustomerProfile


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list_customer.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/add_customer.html'
    success_url = reverse_lazy  ('customer:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = CustomerProfileForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        CustomerProfile.objects.create(
            customer=self.object,
            address=self.request.POST.get('address'),
            debt=self.request.POST.get('debt'),
        )
        return response
    
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


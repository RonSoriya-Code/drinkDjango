from re import S
from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Sale
from .forms import SaleForm

# Create your views here.

class SaleListView(ListView):
     model = Sale
     template_name = 'sale/list_sale.html'
     context_object_name = 'sales'


class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/add_sale.html'
    success_url = reverse_lazy('list_sale:sale_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context['profile_form'] = ProductProfileForm(self.request.POST)
#         else:
#             context['profile_form'] = ProductProfileForm()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         profile_form = context['profile_form']
        
#         if profile_form.is_valid():
#             self.object = form.save()
#             profile = profile_form.save(commit=False)
#             profile.product = self.object
#             profile.save()
#             return super().form_valid(form)
#         else:
#             return self.form_invalid(form)
    
    
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sale/detail_sale.html'
    context_object_name = 'sale'

class SaleUpdateView(UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/edit_sale.html'
    success_url = reverse_lazy('list_sale:sale_list')
    
class SaleDeleteView(DeleteView):
    model = Sale
    template_name = 'sale/delete_sale.html'
    success_url = reverse_lazy('list_sale:sale_list')
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import SaleDetail
from .forms import SaleDetailForm

# Create your views here.

class SaleDetailListView(ListView):
     model = SaleDetail
     template_name = 'saledetail/list_saledetail.html'
     context_object_name = 'saledetails'


class SaleDetailCreateView(CreateView):
    model = SaleDetail
    form_class = SaleDetailForm
    template_name = 'saledetail/add_saledetail.html'
    success_url = reverse_lazy('list_saledetail:saledetail_list')

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
    
    
class SaleDetailDetailView(DetailView):
    model = SaleDetail
    template_name = 'saledetail/detail_saledetail.html'
    context_object_name = 'saledetail'

class SaleDetailUpdateView(UpdateView):
    model = SaleDetail
    form_class = SaleDetailForm
    template_name = 'saledetail/edit_saledetail.html'
    success_url = reverse_lazy('list_saledetail:saledetail_list')
    
class SaleDetailDeleteView(DeleteView):
    model = SaleDetail
    template_name = 'saledetail/delete_saledetail.html'
    success_url = reverse_lazy('list_saledetail:saledetail_list')
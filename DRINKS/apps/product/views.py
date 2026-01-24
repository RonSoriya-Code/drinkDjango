from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.product.forms import ProductForm, ProductProfileForm
from .models import Product, ProductProfile


class ProductListView(ListView):
    model = Product
    template_name = 'product/list_product.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('list_product:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['profile_form'] = ProductProfileForm(self.request.POST)
        else:
            context['profile_form'] = ProductProfileForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        
        if profile_form.is_valid():
            self.object = form.save()
            profile = profile_form.save(commit=False)
            profile.product = self.object
            profile.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/edit_product.html'
    success_url = reverse_lazy('list_product:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            if hasattr(self.object, 'product_profile'):
                context['profile_form'] = ProductProfileForm(self.request.POST, instance=self.object.product_profile)
            else:
                context['profile_form'] = ProductProfileForm(self.request.POST)
        else:
            if hasattr(self.object, 'product_profile'):
                context['profile_form'] = ProductProfileForm(instance=self.object.product_profile)
            else:
                context['profile_form'] = ProductProfileForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']
        
        if profile_form.is_valid():
            self.object = form.save()
            profile = profile_form.save(commit=False)
            profile.product = self.object
            profile.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('list_product:product_list')
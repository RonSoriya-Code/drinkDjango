from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CategoryForm
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list_category.html'
    context_object_name = 'categories'



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/add_category.html'
    success_url = reverse_lazy('list_category:category_list')
    
    
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/detail_category.html'
    context_object_name = 'category'

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/edit_category.html'
    success_url = reverse_lazy('list_category:category_list')
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_url = reverse_lazy('list_category:category_list')

    
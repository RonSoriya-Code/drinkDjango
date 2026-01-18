from django.shortcuts import render

# Create your views here.
def category_list(request):
    return render(request, 'category/index.html')

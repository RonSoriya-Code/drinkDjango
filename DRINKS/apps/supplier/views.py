from django.shortcuts import redirect, render
from apps.supplier.models import Supplier
from apps.supplier.forms import SupplierForm

# Create your views here.

def supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier.html', {'list_supplier': suppliers})

def supplierCreate(request):
    # check if submit form
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_supplier')
    else:
        form = SupplierForm()

    return render(request, 'supplier/add_supplier.html', {'form': form})
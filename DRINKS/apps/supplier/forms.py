from django import form
from .models import Supplier

class SupplierForm(form.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
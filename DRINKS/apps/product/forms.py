from django import forms
from .models import Product, ProductProfile

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ["name", "photo", "quantity", "price", "category"] ## '__all___'
		widgets = {
			"name": forms.TextInput(attrs={"class": "form-control"}),
			"quantity": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
			"price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": 0}),
			"photo": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
			"category": forms.Select(attrs={"class": "form-control"}),
		}
		error_messages = {
            'name': {'required':'Product name is required'},
            'quantity': {'required':'qunatity is required'},
            'price': {'required':'pice is required'},
        }

class ProductProfileForm(forms.ModelForm):
    class Meta:
        model = ProductProfile
        fields = ['address', 'stock_date']
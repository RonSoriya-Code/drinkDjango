from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ["name", "photo", "quantity", "price"] ## '__all___'
		widgets = {
			"name": forms.TextInput(attrs={"class": "form-control"}),
			"quantity": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
			"price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": 0}),
			"photo": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
		}

	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price is not None and price < 0:
			raise forms.ValidationError("Price cannot be negative.")
		return price

	def clean_quantity(self):
		quantity = self.cleaned_data.get("quantity")
		if quantity is None:
			return quantity
		if quantity < 0:
			raise forms.ValidationError("Quantity cannot be negative.")
		return quantity


class ProductSearchForm(forms.Form):
	q = forms.CharField(
		required=False,
		label="",
		widget=forms.TextInput(attrs={"placeholder": "Search products", "class": "form-control"}),
	)

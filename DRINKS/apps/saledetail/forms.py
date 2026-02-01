from django import forms
from .models import SaleDetail

class SaleDetailForm(forms.ModelForm):
	class Meta:
		model = SaleDetail
		fields = '__all__'

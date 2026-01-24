from django import forms
from .models import Customer, CustomerProfile

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        error_messages = {
            'name': {'required':'Customer name is required'},
            'email': {'required':'Email is required'},
            'phone': {'required':'Phone is required'},
            'gender' : {'required' : 'Gender is required'},
        }
        
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['address', 'debt']
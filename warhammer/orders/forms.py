from django import forms

from .models import ProductOrder


class ProductOrderForm(forms.ModelForm):
    
    class Meta:
        model = ProductOrder
        fields = [
            'first_name', 'last_name',
            'email', 'adres',
            'postal_code', 'city'
        ]

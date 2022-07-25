from dataclasses import field
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'brend',
            'article', 
            'quantity', 
            'cost'
        )
        widgets = {
            'brend': forms.TextInput,
            'article': forms.TextInput,
            'quantity': forms.TextInput,
        }
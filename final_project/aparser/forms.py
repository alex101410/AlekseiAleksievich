from dataclasses import field
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'article',
            'brend',
            'cross', 
            'quantity', 
            'cost'
        )
        widgets = {
            'article': forms.TextInput,
            'brend': forms.TextInput,
            'cross': forms.TextInput,
            'quantity': forms.TextInput,
        }
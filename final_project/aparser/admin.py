from django.contrib import admin

from .forms import ProductForm
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'brend', 'cross', 'quantity', 'cost', 'parsing_date')
#    list_filter = ('article')
    form = ProductForm

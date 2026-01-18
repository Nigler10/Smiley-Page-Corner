from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "base_price",
            "category",
            "image",
            "is_available",
        ]

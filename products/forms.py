from django import forms
from .models import ProductList

class add_product(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['title', 'price', 'rating']


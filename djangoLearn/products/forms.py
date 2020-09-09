from django import forms
from .models import Products

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=[
            'title',
            'description',
            'price'
        ]

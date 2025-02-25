from django import forms
from .models import Product
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название продукта',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание продукта',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену продукта',
            }),
        }
from django.forms import fields
from .models import Product,Users
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
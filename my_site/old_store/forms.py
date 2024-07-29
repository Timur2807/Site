from django import forms
from django.contrib.auth.models import Group
from django.forms import Form, ModelForm
from .models import Product


# class ProductForms(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "name", "price", "discription", "discount", "preview"
#
#     images = forms.ImageField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}),
#         )
#
#
# class GroupForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = ["name"]

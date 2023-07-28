from django import forms
from .models import Dish,User_Profile
from django.forms import ModelForm
class DishForm(forms.Form):
    dish_name = forms.CharField(label='Dish Name', required=False)
    price = forms.DecimalField(label='Price', required=False)
class  Loginform(forms.Form):
    username=forms.CharField(label='USERNAME')
    Password=forms.CharField(label='PASSWORD')
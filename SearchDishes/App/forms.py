from django import forms
from .models import Dish
class DishForm(forms.Form):
    dish_name = forms.CharField(label='Dish Name', required=False)
    price = forms.DecimalField(label='Price', required=False)
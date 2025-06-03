# inventory/forms.py
from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['nombre', 'talla', 'color', 'cantidad', 'precio']

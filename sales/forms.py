# sales/forms.py
from django import forms
from .models import Sale, SaleDetail
from inventory.models import Shoe
from django.forms import inlineformset_factory

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = []

class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['zapato', 'cantidad']

SaleDetailFormSet = inlineformset_factory(
    Sale,
    SaleDetail,
    form=SaleDetailForm,
    extra=1,
    can_delete=True
)

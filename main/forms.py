from django import forms
from .models import Consumption

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = (
            'name',
            'category',
            'amount',
            'rating',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'create-consumption-form__input'
            }),
            'category': forms.Select(attrs={
                'class': 'create-consumption-form__input'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'create-consumption-form__input'
            }),
            'rating': forms.Select(attrs={
                'class': 'create-consumption-form__input'
            }),
        }
from django import forms
from django.forms import DateInput, NumberInput, Textarea, Select

from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
            'description': Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'amount_type': Select(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')

        # Automatically populate the month based on the selected date
        cleaned_data['month'] = date.month

        return cleaned_data


class TransactionUpdateForm(forms.ModelForm):
    pass

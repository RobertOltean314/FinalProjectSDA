from django import forms
from django.forms import TextInput, NumberInput, Textarea, DateInput, Select, EmailInput
from .models import Transaction, Category
from datetime import datetime


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']



class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    display_date = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Transaction
        fields = ['display_date', 'description', 'amount', 'amount_type', 'category']
        widgets = {
            'display_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'amount': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
            'amount_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['display_date'].initial = datetime.now().date()


class TransactionUpdateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    display_date = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Transaction
        fields = ['display_date', 'description', 'amount', 'amount_type', 'category']
        widgets = {
            'display_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'amount': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
            'amount_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransactionUpdateForm, self).__init__(*args, **kwargs)
        self.fields['display_date'].initial = datetime.now().date()
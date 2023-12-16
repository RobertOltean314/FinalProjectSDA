from django import forms
from django.forms import DateInput, NumberInput, Textarea, Select

# from transactions.models import Transaction
from .models import Transaction, Category
from datetime import datetime


# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = '__all__'

#         widgets = {
#             'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'amount': NumberInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
#             'description': Textarea(
#                 attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
#             'amount_type': Select(attrs={'class': 'form-control'}),
#             'category': Select(attrs={'class': 'form-control'})
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         date = cleaned_data.get('date')

#         # Automatically populate the month based on the selected date
#         cleaned_data['month'] = date.month

#         return cleaned_data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    #display_date = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}))
    display_date = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Transaction
        fields = ['display_date', 'month', 'description', 'amount', 'amount_type', 'category']
        widgets = {
            # Your widget definitions here
        }

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['display_date'].initial = datetime.now().date()

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date = cleaned_data.get('display_date')

    #     # Automatically populate the month based on the selected date
    #     if date is not None:
    #         cleaned_data['month'] = date.month

    #     return cleaned_data

class TransactionUpdateForm(forms.ModelForm):
    pass

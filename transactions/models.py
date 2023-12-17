from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)


class Transaction(models.Model):
    amount_options = (
        ('income', 'Income'),
        ('expenses', 'Expenses')
    )

    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    amount_type = models.CharField(choices=amount_options, max_length=8)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

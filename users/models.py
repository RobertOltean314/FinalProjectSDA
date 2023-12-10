from django.db import models


# Create your models here.

class UserHistory(models.Model):
    messege = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.messege

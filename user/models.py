from django.db import models
from django.contrib import auth


# Create your models here.
class User(auth.models.User):
    phone = models.CharField(max_length=60,blank=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.username

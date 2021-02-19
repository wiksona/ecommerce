from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=60)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ean_code = models.IntegerField(unique=True)

class Order(models.Model):
   ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Payments(models.Model):
    username = models.CharField(max_length=255)
    amount_money = models.IntegerField()
    commment = models.CharField(max_length=255, blank = True, null = True)
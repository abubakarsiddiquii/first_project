from django.db import models

class Order(models.Model):
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()

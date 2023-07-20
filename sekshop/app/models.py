from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=23)
    price = models.FloatField()
    discription = models.CharField(max_length=300)
    
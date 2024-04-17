# from unicodedata import name
from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=5, decimal_places=2)

def _str_(self):
    return self.name + ' : ' + self.cuisine + ' : ' + str(self.price)

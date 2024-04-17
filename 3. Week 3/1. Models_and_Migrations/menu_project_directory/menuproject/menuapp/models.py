# from unicodedata import name
from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cruisine = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=5, decimal_places=2)

def _str_(self):
    return self.name + ' : ' + self.cruisine + ' : ' + str(self.price)

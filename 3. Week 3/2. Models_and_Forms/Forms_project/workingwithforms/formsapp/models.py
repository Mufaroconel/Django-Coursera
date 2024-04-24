from django.db import models

# Create your models here.
class Applicant(models.Model): 
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=100) 

def records(self):
    return f"{self.name},{self.address}"
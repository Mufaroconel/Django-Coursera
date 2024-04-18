from django.db import models

# Create your models here.
class Applicant(models.Model): 
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=100) 

def records(self):
    return self.name + ':' + self.address
from django import forms    

from .models import Applicant

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'


# class ApplicationForm(forms.Form): 
#     name = forms.CharField(label='Name of Applicant', max_length=50) 
#     address = forms.CharField(label='Address', max_length=100) 
#     posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
#     field = forms.ChoiceField(choices=posts) 

# creating the forms here
# class DemoForm(forms.Form):
#     name = forms.CharField(max_length=100)

# Entering a date
#importing necessary libraries
# from django.forms.widgets import NumberInput

# class DateForm(forms.Form):
#     date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

# Using a choice field

# FAVOURITE_DISH = [
#     ('Pizza', 'Pizza'),
#     ('Burger', 'Burger'),
#     ('Pasta', 'Pasta'),
#     ('Salad', 'Salad'),
#     ('Fries', 'Fries'),
# ]

# class ChoiceForm(forms.Form):
    # favourite_dish = forms.ChoiceField(choices=FAVOURITE_DISH)


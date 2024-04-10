from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Welcome to the newapp home page')


# using namesapce in a view

# Suppose you want the user to be conditionally redirected to the login view from inside another view. You need to obtain the URL of the login view and send the control to it with `HttpResponsePermanentRedirect`.
# from django.http import HttpResponsePermanentRedirect
# from django.urls import reverse

# def myview(request) :
    
#     return HttpResponsePermanentRedirect(reverse('newapp:index'))
from django.urls import path
from . import views
# app_name = 'formsapp'
urlpatterns = [
    path('', views.index, name="index"),
]
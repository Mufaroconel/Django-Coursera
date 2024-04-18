from django.urls import path
from . import views
# app_name = 'formsapp'
urlpatterns = [
    path('', views.form_view, name="form_view"),
]
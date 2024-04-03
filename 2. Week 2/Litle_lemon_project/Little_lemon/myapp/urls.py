# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('', views.home),
#     # path('home/', views.home),
# ]

# Mapping urls with params
from django.urls import path
from . import views

urlpatterns = [
    path('dishes/<str:dish>/', views.menu_items, name='menu_items') # dish=nameofdish
]

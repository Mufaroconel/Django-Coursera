# from django.urls import path
# from . import views

# urlpatterns = [
    # path('', views.home),
    # path('home/', views.home),
# ]

# Mapping urls with params
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('dishes/<str:dish>/', views.menu_items, name='menu_items') # dish=nameofdish
# ]

# from django.urls import path
# from . import views

# urlpatterns = [ 
#     path('', views.index, name="index"),
# ]

# Application namespace

from django.urls import path
from . import views
app_name = 'demoapp'
urlpatterns = [ 
    path('', views.index, name="index"),
    path('notfound/', views.notfound_request, name="notfound_request"),
]

# Adding another app in the project to appreciate the 
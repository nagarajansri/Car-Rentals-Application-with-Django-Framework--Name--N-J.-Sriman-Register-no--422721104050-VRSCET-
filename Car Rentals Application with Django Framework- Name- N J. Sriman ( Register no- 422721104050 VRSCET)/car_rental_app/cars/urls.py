# cars/urls.py

from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.available_cars, name='available_cars'),
    # Add more URL patterns as needed
]

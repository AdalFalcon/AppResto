from django.urls import path
from .views import fetch_and_save_restaurants, search_restaurants

urlpatterns =[
    path('fetch-restaurants/', fetch_and_save_restaurants, name='fetch_restaurants'),
    path('search/', search_restaurants, name='search_restaurants'),
]
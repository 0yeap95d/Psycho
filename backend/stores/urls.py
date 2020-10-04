from django.conf.urls import url, include
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from .views import *


urlpatterns = [
    path('restaurants', store_list),
    path('hotels', hotel_list),
    path('recommend/stores', recommend_store),
    path('recommend/hotels', recommend_hotel),
    path('get_sido', get_sido),
    path('get_gugun', get_gugun),
    path('get_dong', get_dong),
]
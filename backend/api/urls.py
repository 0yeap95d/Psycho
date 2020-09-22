from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"stores", views.StoreViewSet, basename="stores")
router.register(r"reviews", views.ReviewViewSet, base_name="reviews")
router.register(r"hotels", views.HotelViewSet, base_name="hotels")

urlpatterns = [

    ]

urlpatterns += router.urls

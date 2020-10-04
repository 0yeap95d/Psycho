from rest_framework import serializers
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "tel",
            "address1",
            "address2",
            "name",
            "category",
            "pos_x",
            "pos_y",
            ]


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            "id",
            "tel",
            "address1",
            "address2",
            "name",
            "latitude",
            "longitude",
        ]

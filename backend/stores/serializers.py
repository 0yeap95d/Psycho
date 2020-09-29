from rest_framework import serializers
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "store_name",
            "branch",
            "area",
            "tel",
            "address",
            "latitude",
            "longitude",
            "category_list"
            ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "rid",  # 리뷰 고유번호
            "store",  # 음식점 고유번호
            "user",  # 유저 고유번호
            "score",  # 평점
            "content",  # 리뷰 내용
            "reg_time",  # 리뷰 등록 시간
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

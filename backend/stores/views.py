from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from stores.models import *
from stores.serializers import *

# Create your views here.


@csrf_exempt
def store_list(request):
    if request.method == 'GET':
        data = Store.objects.all()
        serializer = StoreSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def review_list(request):
    if request.method == 'GET':
        data = Review.objects.all()
        serializer = ReviewSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def hotel_list(request):
    if request.method == 'GET':
        data = Hotel.objects.all()
        serializer = HotelSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

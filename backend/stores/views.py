from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from stores.models import *
from stores.serializers import *
import json
from api import recommender
import pandas as pd
# Create your views here.

CATEGORY_DICT = {
    2104: ['김밥(도시락)', '냉면집', '분식', '식육(숯불구이)', '탕류(보신용)', '한식', '기타'],
    2107: ['복어취급', '일식', '회집', '횟집', '기타'],
    2109: ['중국식', '외국음식전문점(인도,태국)', '기타'],
    2110: ['경양식', '패밀리레스트랑', '뷔페식', '기타'],
    2112: ['감성주점', '단란주점', '정종/대포집/소주방', '통닭(치킨)', '호프/통닭', '기타']
}


@csrf_exempt
def store_list(request):
    if request.method == 'GET':
        data = Store.objects.all()
        serializer = StoreSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def hotel_list(request):
    if request.method == 'GET':
        data = Hotel.objects.all()
        serializer = HotelSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def recommend_store(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recommender.encode_features(
            data['age'], data['gender'], data['sido'], data['gugun'], data['dong'])
        prediction = recommender.make_prediction()
        category_list = list()
        for category in prediction:
            category_list.extend(CATEGORY_DICT.get(category))
        category_list = list(dict.fromkeys(category_list))
        x_start = float(data['pos_x']) - 0.015
        x_end = float(data['pos_x']) + 0.015
        y_start = float(data['pos_y']) - 0.015
        y_end = float(data['pos_y']) + 0.015
        stores = Store.objects.filter(category__in=category_list, pos_x__range=(
            x_start, x_end), pos_y__range=(y_start, y_end))[:100]
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def recommend_hotel(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        x_start = float(data['pos_x']) - 0.015
        x_end = float(data['pos_x']) + 0.015
        y_start = float(data['pos_y']) - 0.015
        y_end = float(data['pos_y']) + 0.015
        hotels = Hotel.objects.filter(pos_x__range=(x_start, x_end), pos_y__range=(y_start, y_end))[:100]
        serializer = HotelSerializer(hotels, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_sido(request):
    if request.method == 'GET':
        sidos = District.objects.values_list('sido', flat=True).distinct()
        list = []
        for sido in sidos:
            list.append(sido)
        json_data = json.dumps(list, ensure_ascii=False)
        # serializer = DistrictSerializer(sido_dict)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def get_gugun(request):
    if request.method == 'GET':
        sido = request.GET['sido']
        guguns = District.objects.filter(sido__exact=sido).values_list('gugun', flat=True).distinct()
        list = []
        for gugun in guguns:
            list.append(gugun)
        json_data = json.dumps(list, ensure_ascii=False)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def get_dong(request):
    if request.method == 'GET':
        sido = request.GET['sido']
        gugun = request.GET['gugun']
        dongs = District.objects.filter(sido__exact=sido, gugun__exact=gugun).values_list('dong', flat=True)
        list = []
        for dong in dongs:
            list.append(dong)
        json_data = json.dumps(list, ensure_ascii=False)
        return JsonResponse(json_data, safe=False)

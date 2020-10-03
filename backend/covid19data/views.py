from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *

# Create your views here.


@csrf_exempt
def getCovid19Info(request):
    if request.method == 'GET':
        data = Covid19Info.objects.all()
        serializer = Covid19InfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def getCovid19GenAgeInfo(request):
    if request.method == 'GET':
        data = Covid19GenAgeInfo.objects.all()
        serializer = Covid19GenAgeInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def getCovid19SidoInfo(request):
    if request.method == 'GET':
        data = Covid19SidoInfo.objects.all()
        serializer = Covid19SidoInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

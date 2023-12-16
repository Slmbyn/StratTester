from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TestSerializer, ResultSerializer
from .models import Test, Result
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import requests
from decouple import config

STOCK_API_KEY = config('STOCK_API_KEY')



class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

def stock_data(request):
    ticker = Test.ticker
    date = Test.date
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{date}/{date}?adjusted=true&sort=asc&limit=120&apiKey={STOCK_API_KEY}'
    print('THE URL IS:::', url)
    response = requests.get(url)
    print('THE RESPONSE IS:::', response)
    data = response.json()
    print('THE DATA IS:', data)

@api_view(['POST'])
def test_strategy(request):
    if request.method == 'POST':
# take request & create the test instance in the db
        test_data = JSONParser().parse(request)
        test_serializer = TestSerializer(data=test_data)
        print('THIS IS THE TEST DATA', test_serializer)
        if test_serializer.is_valid():
            test_serializer.save()
            return JsonResponse(test_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# calculate values for Results model, save to db , then return as a json response (this part will require the api setup first)
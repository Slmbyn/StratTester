from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestSerializer, ResultSerializer
from .models import Test, Result

class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
from rest_framework import serializers
from .models import Test, Result

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'strategy', 'ticker', 'date')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'PL_percent', 'PL_abs', 'volume','entry_price','exit_price', 'test')
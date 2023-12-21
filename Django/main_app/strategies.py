from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TestSerializer, ResultSerializer
from .models import Test, Result
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import requests
from decouple import config
from rest_framework.response import Response


STOCK_API_KEY = config('STOCK_API_KEY')




def orb_strategy(test_data):
    # SEND API REQ USING SUBMITTED TEST DATA
    ticker = test_data["ticker"]
    date = test_data["date"]
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{date}/{date}?adjusted=true&sort=asc&limit=120&apiKey={STOCK_API_KEY}'
    print('API URL IS!!!!', api_url)
    api_response = requests.get(api_url)
    print('API RESPONSE IS:', api_response)
    if api_response.status_code == 200:
        api_data = api_response.json()
        print('API DATA IS:', api_data)
        first_five_mins = api_data['results'][0]
        high_first_five = first_five_mins['h']
        low_first_five = first_five_mins['l']

        entry_price = None
        exit_price = None
        PL_abs = None
        PL_percent = None

        for idx, data_point in enumerate(api_data['results'][1:]):
            current_price = data_point['c']
            volume = data_point['v']
            current_index = idx + 1
            # Long Position
            if current_price > high_first_five:
                entry_price = current_price
                print('CURRENT INDEX', current_index)
                print('CURRENT PRICE', entry_price)
                for exit_point in api_data['results'][current_index:]:
                    exit_price_candidate = exit_point['c']
                    if exit_price_candidate >= (entry_price + 1):
                        print('EXIT WITH A PROFIT')
                        result_details = {
                            'PL_percent': round(((exit_price_candidate - entry_price) / entry_price),4),
                            'PL_abs': round( exit_price_candidate - entry_price, 2),
                            'volume': volume,
                            'entry_price': entry_price,
                            'exit_price': exit_price_candidate,
                            # 'test': test_serialize
                        }
                        print('long-profit RESULT DETAILS ARE:', result_details)
                        return result_details
                    elif exit_price_candidate <= (entry_price - 0.50):
                        print('CURRENT INDEX', current_index)
                        print('EXIT WITH A LOSS')
                        result_details = {
                            'PL_percent': round(((exit_price_candidate - entry_price) / entry_price),4),
                            'PL_abs': round( exit_price_candidate - entry_price, 2),
                            'volume': volume,
                            'entry_price': entry_price,
                            'exit_price': exit_price_candidate,
                            # 'test': test_serializer.instance
                        }
                        print('long-loss RESULT DETAILS ARE:', result_details)
                        return result_details
                # If none of the exit conditions are met, handle here
                result_details = {
                    'PL_percent': 0.00,
                    'PL_abs': 0.00,
                    'volume': volume,
                    'entry_price': entry_price,
                    'exit_price': entry_price,
                    # 'test': test_serializer
                }
                print('Long-no-exit RESULT DETAILS ARE:', result_details)
                return result_details

            # Short Position
            elif current_price < low_first_five:
                entry_price = current_price

                for exit_point in api_data['results'][current_index:]:
                    exit_price_candidate = exit_point['c']
                    if exit_price_candidate <= (entry_price - 1):
                        print('EXIT WITH A PROFIT')
                        result_details = {
                            'PL_percent': round(((entry_price - exit_price_candidate) / entry_price), 4),
                            'PL_abs': round( exit_price_candidate - entry_price, 2),
                            'volume': volume,
                            'entry_price': entry_price,
                            'exit_price': exit_price_candidate,
                            # 'test': test_serializer
                        }
                        print('short-profit RESULT DETAILS ARE:', result_details)
                        return result_details
                    elif exit_price_candidate >= (entry_price + 0.50):
                        print('EXIT WITH A LOSS')
                        result_details = {
                            'PL_percent': round(((exit_price_candidate - entry_price) / entry_price), 4),
                            'PL_abs': round((entry_price - exit_price_candidate), 2),
                            'volume': volume,
                            'entry_price': entry_price,
                            'exit_price': exit_price_candidate,
                            # 'test': test_serializer
                        }
                        print('short-loss RESULT DETAILS ARE:', result_details)
                        return result_details

                # If none of the exit conditions are met, handle here
                result_details = {
                    'PL_percent': 0,
                    'PL_abs': 0,
                    'volume': volume,
                    'entry_price': entry_price,
                    'exit_price': exit_price_candidate,
                    # 'test': test_serializer
                }
                print('no-short-exit RESULT DETAILS ARE:', result_details)
                return result_details
























# @api_view(['POST'])
# def test_strategy(request):
#     if request.method == 'POST':
# # take request & create the test instance in the db
#         test_data = JSONParser().parse(request)
#         test_serializer = TestSerializer(data=test_data)
#         if test_serializer.is_valid():
#             check_new_test = test_serializer.save()
#             print('TEST SERIALIZER AFTER SAVE', check_new_test)
#         # invoke trade strategy here
#         orb(test_data, test_serializer)

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
                    if exit_price_candidate >= (entry_price + 0.20):
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
                    elif exit_price_candidate <= (entry_price - 0.10):
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
                    if exit_price_candidate <= (entry_price - 0.20):
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
                    elif exit_price_candidate >= (entry_price + 0.10):
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

    # # If no conditions are met, handle here
    # return {
    #     'PL_percent': 0.00,
    #     'PL_abs': 0.00,
    #     'volume': 0,
    #     'entry_price': 0.00,
    #     'exit_price': 0.00,
    #     # 'test': test_serializer
    # }




# def orb_strategy(test_data):
    # SEND API REQ USING SUBMITTED TEST DATA
    # ticker = test_data["ticker"]
    # date = test_data["date"]
    # api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{date}/{date}?adjusted=true&sort=asc&limit=120&apiKey={STOCK_API_KEY}'
    # print('API URL IS!!!!', api_url)
    # api_response = requests.get(api_url)
    # print('API RESPONSE IS:', api_response)
    # if api_response.status_code == 200:
    #     api_data = api_response.json()
#         print('API DATA IS:', api_data)
#         first_five_mins = api_data['results'][0]
#         # print('FIRST FIVE MIN!!!!:', first_five_mins)
#         second_five_mins = api_data['results'][1]
#         # print('SECOND FIVE MIN!!!!:', second_five_mins)
#         high_first_five = first_five_mins['h']
#         print('HIGH OF FIRST CANDLE!!!!:', high_first_five)
#         low_first_five = first_five_mins['l']
#         # print('LOW OF FIRST CANDLE!!!!:', low_first_five)
#         entry_price = None
#         exit_price = None
#         PL_abs = None
#         PL_percent = None
#         for data_point in api_data['results'][1:]:
#             print('DATA POINT', data_point)
#             current_price = data_point['c']
#             volume = data_point['v']
#             print('CURRENT PRICE', current_price)
#             # Long Position
#             if current_price > high_first_five:
#                 entry_price = current_price
#                 if entry_price:
#                     print('ENTRY PRICE EVALUATED. Line 58:', entry_price)
#             # RUNS UNTIL HERE!!!!
#                     for exit_point in api_data['results']:
#                         exit_price = exit_point['c']
#                         if exit_price >= (entry_price + 0.02):
#                             print('EXIT WITH A PROFIT')
#                             result_details = {
#                                 'PL_percent': ((current_price - entry_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                                 # 'test': test_serialize
#                             }
#                             print('long-profit RESULT DETAILS ARE:', result_details)
#                             return result_details
#                         elif current_price <= (entry_price - 0.01):
#                             print('EXIT WITH A LOSS')
#                             result_details = {
#                                 'PL_percent': ((current_price - entry_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                                 # 'test': test_serializer.instance
#                             }
#                             print('long-loss RESULT DETAILS ARE:', result_details)
#                             return result_details
#                         else:
#                             result_details = {
#                                 'PL_percent': 0.00,
#                                 'PL_abs': 0.00,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': current_price,
#                                 # 'test': test_serializer
#                             }
#                             print('Long-no-exit RESULT DETAILS ARE:', result_details)
#                             return result_details
#             # Short Position
#             elif current_price < low_first_five:
#                 entry_price = current_price
#                 if entry_price:
#                     print('ENTRY PRICE EVALUATED FOR TOM. line 112', entry_price)
#                     for exit_point in api_data['results']:
#                         exit_price = exit_point['c']
#                         if current_price <= (entry_price - 0.10):
#                             print('EXIT WITH A PROFIT')
#                             result_details = {
#                                 'PL_percent': ((current_price - entry_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                                 # 'test': test_serializer
#                             }
#                             print('short-profit RESULT DETAILS ARE:', result_details)
#                 # WORKS UNTIL HERE!!!!
#                             # Add logic to save this to Result Model
#                             # result_serializer = ResultSerializer(data=result_details)
#                             # if result_serializer.is_valid():
#                             #     result_serializer.save()
#                             #     # return Response(result_serializer.data, status=status.HTTP_201_CREATED)
#                             # else:
#                             #     return Response({'message': 'FAILED TO TAKE PROFIT'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#                             return result_details
#                         elif current_price >= (entry_price + 0.05):
#                             print('EXIT WITH A LOSS')
#                             result_details = {
#                                 'PL_percent': ((entry_price - exit_price) / entry_price),
#                                 'PL_abs': abs(entry_price - current_price),
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                                 # 'test': test_serializer
#                             }
#                             print('short-loss RESULT DETAILS ARE:', result_details)
#                             # Add logic to save this to Result Model
#                             # result_serializer = ResultSerializer(data=result_details)
#                             # if result_serializer.is_valid():
#                             #     result_serializer.save()
#                             #     # return Response(result_serializer.data, status=status.HTTP_201_CREATED)
#                             # else:
#                             #     return Response({'message': 'FAILED TO TAKE LOSS'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#                             return result_details
#                         else:
#                             result_details = {
#                                 'PL_percent': 0,
#                                 'PL_abs': 0,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                                 # 'test': test_serializer
#                             }
#                             print('no-short-exit RESULT DETAILS ARE:', result_details)
#                             # Add logic to save this to Result Model
#                             # result_serializer = ResultSerializer(data=result_details)
#                             # if result_serializer.is_valid():
#                             #     result_serializer.save()
#                             return result_details
#                         # return Response({'message': 'No exit criteria met.'},result_details, status=status.HTTP_200_OK)
#         else:
#             pass
#             # return Response({'message': f'API request failed with status code {api_response.status_code}.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#     #     return Response(test_serializer.data, status=status.HTTP_201_CREATED)
#     # return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # calculate values for Results model, save to db , then return as a json response (this part will require the api setup first)
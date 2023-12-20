from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from .serializers import TestSerializer, ResultSerializer, UserSerializer
from .models import Test, Result, User
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import requests
from decouple import config
from .strategies import orb_strategy
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


STOCK_API_KEY = config('STOCK_API_KEY')

@api_view(['POST'])
def login_view(request):
    print('login request is:', request.data)
    # username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register_view(request):
    print('request is:', request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()
    logout(request)
    return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # authenticate
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             context = {'error': 'Invalid username or password'}
#         login(request, user)
#         # add a line here sending user info to React






class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class ResultView(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


@api_view(['POST'])
def test_strategy(request):
    if request.method == 'POST':
        # take request & create the test instance in the db
        test_data = JSONParser().parse(request)
        test_serializer = TestSerializer(data=test_data)
        if test_serializer.is_valid():
            test_instance = test_serializer.save()
            # invoke trade strategy here
            results = orb_strategy(test_data)
            results['test'] = test_instance.id
            print('RESULT IN VIEW:', results)
            # Save Result to database
            result_serializer = ResultSerializer(data=results)
            print('IS RESULT VALID?', result_serializer.is_valid())
            if result_serializer.is_valid():
                result_serializer.save()
            # Send result data for React
            return JsonResponse(results, status=status.HTTP_201_CREATED)
    return Response({'message': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)











# def stock_data(request):
#     ticker = Test.ticker
#     date = Test.date
#     url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{date}/{date}?adjusted=true&sort=asc&limit=120&apiKey={STOCK_API_KEY}'
#     print('THE URL IS:::', url)
#     response = requests.get(url)
#     print('THE RESPONSE IS:::', response)
#     data = response.json()
#     print('THE DATA IS:', data)

# @api_view(['POST'])
# def test_strategy(request):
#     if request.method == 'POST':
# # take request & create the test instance in the db
#         test_data = JSONParser().parse(request)
#         test_serializer = TestSerializer(data=test_data)
#         if test_serializer.is_valid():
#             check_new_test = test_serializer.save()
#             print('TEST SERIALIZER AFTER SAVE', check_new_test)
#         ticker = test_data["ticker"]
#         date = test_data["date"]
#         api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/5/minute/{date}/{date}?adjusted=true&sort=asc&limit=120&apiKey={STOCK_API_KEY}'
#         print('API URL IS!!!!', api_url)
#         api_response = requests.get(api_url)
#         print('API RESPONSE IS:', api_response)
#         if api_response.status_code == 200:
#             api_data = api_response.json()
#             print('API DATA IS:', api_data)
#             first_five_mins = api_data['results'][0]
#             # print('FIRST FIVE MIN!!!!:', first_five_mins)
#             second_five_mins = api_data['results'][1]
#             # print('SECOND FIVE MIN!!!!:', second_five_mins)
#             high_first_five = first_five_mins['h']
#             print('HIGH OF FIRST CANDLE!!!!:', high_first_five)
#             low_first_five = first_five_mins['l']
#             # print('LOW OF FIRST CANDLE!!!!:', low_first_five)
#             entry_price = None
#             exit_price = None
#             PL_abs = None
#             PL_percent = None
#             for data_point in api_data['results'][1:]:
#                 print('DATA POINT', data_point)
#                 current_price = data_point['c']
#                 volume = data_point['v']
#                 print('CURRENT PRICE', current_price)
#                 # Long Position
#                 if current_price > high_first_five:
#                     entry_price = current_price
#                     if entry_price:
#                         print('ENTRY PRICE EVALUATED FOR TOM', entry_price)
#                         if current_price > 130.47:
#                             print('EXIT WITH A PROFIT')
#                             result_details = {
#                                 'PL_percent': ((current_price - entry_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': current_price,
#                                 'test': test_serializer.instance
#                             }
#                             print('RESULT DETAILS ARE:', result_details)
#                 # WORKS UNTIL HERE!!!!
#                             # Add logic to save this to Result Model
#                             result_serializer = ResultSerializer(data=result_details)
#                             if result_serializer.is_valid():
#                                 result_serializer.save()
#                                 return JsonResponse({'message': 'Strategy Testing Complete.'}, status=status.HTTP_201_CREATED)
#                             else:
#                                 return JsonResponse({'message': 'Strategy Testing Failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#                         if current_price <= 130.3:
#                             print('EXIT WITH A LOSS')
#                             result_details = {
#                                 'PL_percent': ((current_price - entry_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': current_price,
#                                 'test': test_serializer.instance
#                             }
#                             print('RESULT DETAILS ARE:', result_details)
#                             # Add logic to save this to Result Model
#                             result_serializer = ResultSerializer(data=result_details)
#                             if result_serializer.is_valid():
#                                 result_serializer.save()
#                                 return JsonResponse({'message': 'Strategy Testing Complete.'}, status=status.HTTP_201_CREATED)
#                             else:
#                                 return JsonResponse({'message': 'Strategy Testing Failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#                         else:
#                             print('Here is the error')
#                 # Short Position
#                 elif current_price < low_first_five:
#                     entry_price = current_price
#                     if entry_price:
#                         if current_price <= entry_price / 1.03 or current_price >= entry_price * 0.99:
#                             exit_price = current_price
#                             result_details = {
#                                 'PL_percent': ((entry_price - exit_price) / entry_price),
#                                 'PL_abs': entry_price - current_price,
#                                 'volume': volume,
#                                 'entry_price': entry_price,
#                                 'exit_price': exit_price,
#                             }
#                             # Add logic to save this to Result Model
#                             result_serializer = ResultSerializer(data=result_details)
#                             if result_serializer.is_valid():
#                                 result_serializer.save(test=test_serializer.instance)
#                                 return JsonResponse({'message': 'Strategy Testing Complete.'}, status=status.HTTP_201_CREATED)
#                             else:
#                                 return JsonResponse({'message': 'Strategy Testing Failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        

#         else:
#             return JsonResponse({'message': f'API request failed with status code {api_response.status_code}.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#         #     return JsonResponse(test_serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # calculate values for Results model, save to db , then return as a json response (this part will require the api setup first)
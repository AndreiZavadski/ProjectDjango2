from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


hello_dict = {
    "december": 'первый месяц зимы',
    "january": 'второй месяц зимы',
    "february": 'последний месяц зимы',
    "march": 'первый месяц весны',
    "april":  'второй месяц весны',
    "may": 'третий месяц весны'
}

def index(request, seasons):
    a = hello_dict.get(seasons, None)
    if a:
        return HttpResponse(a)
    else:
        return HttpResponseNotFound(f'{seasons} месяца не существует!')

# def index(request, seasons):
#     if seasons == 'december':
#         return HttpResponse('первый месяц зимы')
#     elif seasons == 'january':
#         return HttpResponse('второй месяц зимы ')
#     elif seasons == 'february':
#         return HttpResponse('последний месяц зимы')
#     elif seasons == 'march':
#         return HttpResponse('первый месяц весны')
#     elif seasons == 'april':
#         return HttpResponse('второй месяц весны')
#     elif seasons == 'may':
#         return HttpResponse('третий месяц весны')
#     elif seasons == 'june':
#         return HttpResponse('первый месяц лета')
#     elif seasons == 'july':
#         return HttpResponse('второй месяц лета')
#     elif seasons == 'august':
#         return HttpResponse('третий месяц лета')
#     elif seasons == 'september':
#         return HttpResponse('первый месяц осени')
#     elif seasons == 'october':
#         return HttpResponse('второй месяц осени')
#     elif seasons == 'november':
#         return HttpResponse('третий месяц осени')
#     else:
#         return HttpResponseNotFound('Такого месяца не существует!')

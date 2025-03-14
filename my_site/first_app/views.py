from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

articles = {
    'sports' : 'Sports_view',
    'finance' : 'Finance_view',
    'pocil' : 'pocil_view'
}

def news_view(request, topic):
    return HttpResponse(articles[topic])
def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def hello(request, name):
    return HttpResponse(f"Hello {name}")

def sum(request, a: int, b: int):
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is {result}")

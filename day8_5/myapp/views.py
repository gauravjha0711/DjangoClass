from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showname(request,name):
    return HttpResponse(f"My name is {name}")

def sum(request,a,b):
    c = a + b
    return HttpResponse(f"Sum of {a} and {b} is {c}")


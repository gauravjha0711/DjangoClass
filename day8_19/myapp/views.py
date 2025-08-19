from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
# Create your views here.

def indexpage(request):
    return render(request,'myapp/child.html')

def abc(request):
    return render(request,'myapp/abc.html')
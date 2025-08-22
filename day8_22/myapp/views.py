from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
# Create your views here.

def indexpage(request):
    contex = {"username":"Gaurav","age":25,"location":"Patna, Bihar"}
    return render(request,'myapp/child.html',contex)
def new(request):
    return render(request,'myapp/new.html')
def abc(request):
    return render(request,'myapp/abc.html')
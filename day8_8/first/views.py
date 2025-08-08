from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
# Create your views here.
def json(request):
    data = {
        "name" : "Gaurav",
        "age" : 20,
        "city" : "Patna"
    }
    return JsonResponse(data)

def apidata(request):
    response = requests.get("https://api.sampleapis.com/futurama/characters")
    data = response.json()
    return JsonResponse(data, safe=False)
    # return HttpResponse(response)
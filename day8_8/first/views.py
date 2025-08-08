from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
def json(request):
    data = {
        "name" : "Gaurav",
        "age" : 20,
        "city" : "Patna"
    }
    return JsonResponse(data)
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hellofunction(request):
    # return HttpResponse("Hello, World!")
    # return HttpResponse("<h1>Hello, World!</h1>")
    name = "Gaurav Jha"
    place = "Patna"
    # return HttpResponse("My name is "+name+" and I am from "+place+".")
    # return HttpResponse(f"My name is {name} and I am from {place}.")
    a=10
    b=20
    return HttpResponse(f"The sum of {a} and {b} is {a+b}.")

def mydict(request):
    items = {
        "a" : "about a",
        "b" : "about b",
        "c" : "about c",
    }
    context = "Menu Items:<br>"
    for key, value in items.items():
        context+= f"<li>{key} : {value}</li>"
    return HttpResponse(context)
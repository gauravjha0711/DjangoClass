from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showname(request,name):
    return HttpResponse(f"My name is {name}")

def sum(request,a,b):
    c = a + b
    return HttpResponse(f"Sum of {a} and {b} is {c}")

def getval(request):
    value = request.GET.get('val')
    # http://127.0.0.1:8000/getval/?val=Gaurav
    return HttpResponse(f"The value is {value}")

def getsum(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    # http://127.0.0.1:8000/getsum/?a=5&b=10
    return HttpResponse(f"Sum of {a} and {b} is {a+b}")

def sumtry(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    operation = request.GET.get('c')
    try:
        a =float(a)
        b =float(b)
        if operation == 'add':
            return HttpResponse(f"Sum of {a} and {b} is {a+b}")
        elif operation == 'sub':
            return HttpResponse(f"Difference of {a} and {b} is {a-b}")
        elif operation == 'mul':
            return HttpResponse(f"Product of {a} and {b} is {a*b}")
        elif operation == 'div':
            if b != 0:
                return HttpResponse(f"Division of {a} by {b} is {a/b}")
            else:
                return HttpResponse("Division by zero is not allowed.")
        else:
            return HttpResponse("Invalid operation. Give add, sub, mul, or div.")
        # http://127.0.0.1:8000/sumtry/?a=5&b=10&c=add
        return HttpResponse(f"Sum of {a} and {b} is {a+b}")
    except ValueError:
        return HttpResponse("Please provide valid numbers for a and b.")


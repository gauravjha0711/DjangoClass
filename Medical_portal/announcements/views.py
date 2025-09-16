from django.shortcuts import render

def home(request):
    return render(request, 'announcements/home.html', {"message": "Welcome to Medical Portal"})

def calculator(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            op = request.POST.get('op')

            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                if b == 0:
                    raise ZeroDivisionError
                result = a / b
        except ZeroDivisionError:
            error = "Division by zero is not allowed!"
        except:
            error = "Invalid input!"

    return render(request, 'announcements/calculator.html', {"result": result, "error": error})

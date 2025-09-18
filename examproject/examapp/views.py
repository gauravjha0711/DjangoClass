from django.shortcuts import render

def results_view(request):
    results = [35, 42, 65, 90, 55, 30, 80, 49]
    pass_mark = 50
    pass_list = [r for r in results if r >= pass_mark]
    fail_list = [r for r in results if r < pass_mark]

    context = {
        'total': len(results),
        'passed': len(pass_list),
        'failed': len(fail_list),
        'pass_percentage': (len(pass_list) / len(results)) * 100,
    }
    return render(request, 'results.html', context)


def profile_view(request, username, age):
    if age >= 18:
        message = f"Welcome {username}!, you are eligible."
    else:
        message = f"Sorry {username}, you are underage."
    return render(request, 'profile.html', {'message': message})

students = [
    {'id': 1, 'name': 'Hariom', 'age': 20, 'course': 'B.Tech CSE'},
    {'id': 2, 'name': 'Gaurav', 'age': 21, 'course': 'BCA'},
    {'id': 3, 'name': 'Priya', 'age': 19, 'course': 'MBA'},
    {'id': 4, 'name': 'Aman', 'age': 22, 'course': 'MCA'},
]

def students_list(request):
    return render(request, 'students_list.html', {'students': students})

def student_details(request, id):
    # find student by id
    student = next((s for s in students if s['id'] == id), None)
    return render(request, 'student_details.html', {'student': student})
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

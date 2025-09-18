from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.results_view, name='results'),
    path('profile/<str:username>/<int:age>/', views.profile_view, name='profile'),
    path('students/', views.students_list, name='students_list'),
    path('students/<int:id>/', views.student_details, name='student_details'),
]

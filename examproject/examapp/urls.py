from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.results_view, name='results'),
    path('profile/<str:username>/<int:age>/', views.profile_view, name='profile'),
]

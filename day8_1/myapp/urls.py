from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.hellofunction),
    path('mydict/',views.mydict),
    path('mylist/',views.mylist),
]
from django.urls import path,re_path
from . import views
urlpatterns = [
    
    path('indexpage/',views.indexpage),
    path('abc/',views.abc),
]

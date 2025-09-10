from django.urls import path,re_path
from . import views
urlpatterns = [
    
    path('indexpage/',views.indexpage),
    path('abc/',views.abc),
    path('new/',views.new),

    path('hello/',views.hello),
    path('student/',views.hello),
]

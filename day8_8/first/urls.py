from django.urls import path,re_path
from . import views
urlpatterns = [
    path('json/',views.json),
    path('apidata/',views.apidata),
    re_path(r'^regex/(?P<username>[a-zA-Z]+)/$', views.regex),
]

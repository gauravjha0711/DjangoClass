# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('new/', views.create_post, name='post_create'),        # /blog/new/
    path('<int:pk>/', views.post_detail, name='post_detail'),   # /blog/1/
]

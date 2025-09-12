from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_gallery),
    path('<int:count>/', views.show_gallery),  
]

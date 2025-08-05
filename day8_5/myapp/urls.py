from django.urls import path
from . import views
urlpatterns = [
    path('showname/<str:name>',views.showname),

    path('sum/<int:a>/<int:b>',views.sum),
]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("last/", views.redirect_to_last_product, name="redirect_to_last_product"),
    path("color/", views.color_preference, name="color_preference"),
]

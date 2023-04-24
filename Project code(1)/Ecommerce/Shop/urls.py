from django.urls import path

from . import views

app_name = "Shop" 

urlpatterns = [
    path("", views.home, name="home"),
    path("sell", views.sell, name="sell"),
    path("service", views.service, name="service"),
    path("single", views.single, name="single")
]
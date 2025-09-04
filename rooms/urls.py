from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello),
    path("time", views.say_hello_with_time),
    path("request", views.request_info),
]

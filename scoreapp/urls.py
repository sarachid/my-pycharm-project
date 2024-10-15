from django.urls import path

from scoreapp import views

urlpatterns = [
    path('',views.home),
    path('read',views.read_fun),
]
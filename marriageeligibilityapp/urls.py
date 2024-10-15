from django.urls import path

from marriageeligibilityapp import views

urlpatterns = [
    path('',views.home),
    path('read',views.read_fun),
]
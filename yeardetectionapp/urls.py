from django.urls import path

from yeardetectionapp import views

urlpatterns = [
    path('',views.home),
    path('read',views.year_fun),
]
from django import urls
from django.urls import path

from authorization import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
]

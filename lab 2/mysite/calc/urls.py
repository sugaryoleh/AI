from django.urls import path

from calc import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('charts/', views.charts, name='charts'),
    path('info/', views.info, name='info'),
    path('info_view/', views.info_view, name='info_view'),
]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from diseases import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/complain/<int:id>', views.complain, name='complain'),
    path('signup/<int:role>/', views.signup, name='signup'),
    path('login/', views._login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='auth/login.html')),
    path('accounts/', include('django.contrib.auth.urls')),
]
from django.urls import path

from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:poll_id>/<int:question_id>', views.detail, name='detail'),
    path('<int:poll_id>/', views.detail_redirect, name='detail_redirect'),
    path('<int:poll_id>/<int:question_id>/vote', views.vote, name='vote'),
    path('chart/', views.chart, name='chart'),
]
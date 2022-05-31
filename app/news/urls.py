from django.urls import path

from news.views import index, alone, statistics

app_name = 'news'
urlpatterns = [
    path('alone/<int:pk>/', alone, name='alone'),
    path('statistic/', statistics, name='stat'),
    path('', index, name='index'),
]

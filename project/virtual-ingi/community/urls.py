from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home, name='user'),
    #path('create', views.Create, name='input'),
    path('create', views.Date, name='date')
]
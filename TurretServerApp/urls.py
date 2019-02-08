from django.conf.urls import url
from django.urls import path
from TurretServerApp import views

urlpatterns = [
    #path('<str:par>/', views.index),
    path('', views.index, name='index'),
    path('test/', views.test, name='test')
]


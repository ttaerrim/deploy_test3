from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld', views.helloworld, name='helloworld'),
]

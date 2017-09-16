from django.conf.urls import url
from django.shortcuts import render, redirect

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

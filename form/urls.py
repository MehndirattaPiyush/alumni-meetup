from django.conf.urls import url

from django.shortcuts import render 
from . import views

app_name = 'form'

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^fill', views.AddStudent.as_view(), name = 'add-student')
]

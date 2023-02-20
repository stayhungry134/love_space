"""
name: urls.py
create_time: 2023-02-16
author: Ethan White

Description:
"""
from django.urls import path
from love_record import views

app_name = 'love_record'

urlpatterns = [
    path('', views.index, name='index'),
]

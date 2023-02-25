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
    # 故事相关的 url
    path('our_story/', views.our_story, name='our_story'),
    path('our_story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('our_story/add_edit/<int:story_id>/', views.add_edit_story, name='add_edit_story'),
]

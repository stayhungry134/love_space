"""
name: form.py
create_time: 2023-02-16
author: Ethan White

Description: 
"""
from django.forms import ModelForm
from mdeditor.fields import MDTextFormField
from love_record.models import OurStory


class OurStoryForm(ModelForm):
    content = MDTextFormField()

    class Meta:
        model = OurStory
        fields = ['story_title', 'story_time', 'story_img']

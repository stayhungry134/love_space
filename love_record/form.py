"""
name: form.py
create_time: 2023-02-16
author: Ethan White

Description: 
"""
from django import forms
from mdeditor.fields import MDTextFormField
from love_record.models import OurStory


class OurStoryForm(forms.Form):
    story_time = OurStory.story_time
    story_img = OurStory.story_img
    centent = MDTextFormField()
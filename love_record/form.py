"""
name: form.py
create_time: 2023-02-16
author: Ethan White

Description: 
"""
from django.forms import ModelForm
from django.forms import forms
from mdeditor.fields import MDTextFormField
from love_record.models import OurStory


class OurStoryForm(forms.Form):
    content = MDTextFormField(label='故事内容')

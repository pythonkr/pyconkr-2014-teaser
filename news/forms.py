# -*- coding:utf-8 -*-
from django import forms
from news.models import News

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
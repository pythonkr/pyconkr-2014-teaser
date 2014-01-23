# coding=utf-8
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_created=True)

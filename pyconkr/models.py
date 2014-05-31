# -*- coding:utf-8 -*-
from django.db import models


class Speaker(models.Model):
    picture = models.ImageField(upload_to='speaker/')
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    intro = models.CharField(max_length=1024)
    link = models.URLField(max_length=512)

    def __unicode__(self):
        return self.name


class Program(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker)
    start = models.DateTimeField()
    description = models.TextField()


class Sponsor(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='sponsor/')
    link = models.URLField(max_length=512)




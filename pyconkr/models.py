# -*- coding:utf-8 -*-
from django.db import models
from pyconkr.lib import CacheDeleteMixin


class Speaker(CacheDeleteMixin, models.Model):
    picture = models.ImageField(upload_to='speaker/')
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    intro = models.CharField(max_length=1024)
    link = models.URLField(max_length=512)

    template_cache_names = ['speakers']

    def __unicode__(self):
        return self.name


class Program(CacheDeleteMixin, models.Model):
    title = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker)
    start = models.DateTimeField()
    description = models.TextField()

    template_cache_names = ['programs']

    def __unicode__(self):
        return self.title


class Sponsor(CacheDeleteMixin, models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='sponsor/')
    link = models.URLField(max_length=512)

    template_cache_names = ['sponsors']

    def __unicode__(self):
        return self.title




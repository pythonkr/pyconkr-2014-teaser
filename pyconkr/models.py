# -*- coding:utf-8 -*-
from PIL import Image
from django.conf import settings
from django.db import models
from solo.models import SingletonModel

from pyconkr.lib import CacheDeleteMixin


class Speaker(CacheDeleteMixin, models.Model):
    picture = models.ImageField(upload_to='speaker/')
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    intro = models.TextField(default=None)
    link = models.URLField(max_length=512)

    template_cache_names = ['speakers']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Speaker, self).save(*args, **kwargs)
        image = Image.open(self.picture.path)
        speaker_picture_size = settings.IMAGE_SIZES['speaker']
        width, height = image.size
        if width > speaker_picture_size[0]:
            image.thumbnail(settings.IMAGE_SIZES['speaker'], Image.ANTIALIAS)
            image.save(self.picture.path)
        del image


class Room(models.Model):
    name = models.CharField(max_length=50)

    def programs(self):
        return self.program_set.all()
    
    def __unicode__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)

    def programs(self):
        return self.program_set.all()

    def __unicode__(self):
        return self.name

class Program(CacheDeleteMixin, models.Model):
    room = models.ForeignKey(Room, default=None)
    track = models.ForeignKey(Track, default=None, null=True)
    title = models.CharField(max_length=100)
    speaker = models.ForeignKey(Speaker)
    start = models.DateTimeField()
    description = models.TextField()

    template_cache_names = ['programs']

    class Meta:
        ordering = ['start']

    def __unicode__(self):
        return self.title


class Sponsor(CacheDeleteMixin, models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='sponsor/')
    link = models.URLField(max_length=512)

    template_cache_names = ['sponsors']

    def __unicode__(self):
        return self.title


class SiteConfiguration(SingletonModel):
    proposal_now = models.BooleanField(default=True)
    registration_url = models.URLField()

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"


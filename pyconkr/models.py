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


class Program(CacheDeleteMixin, models.Model):
    ROOM_CHOICES = (
        ('a', '젬마홀'),
    )
    room = models.CharField(max_length=2, choices=ROOM_CHOICES,
                            default='a')
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


class SiteConfiguration(SingletonModel):
    proposal_now = models.BooleanField(default=True)

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"


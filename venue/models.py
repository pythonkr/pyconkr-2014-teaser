# coding=utf-8
from django.conf import settings
from django.db import models


class Place(models.Model):
    TYPE_TO_EAT = 100
    TYPE_TO_SLEEP = 200

    TYPES = (
        (TYPE_TO_EAT, 'Place to Eat'),
        (TYPE_TO_SLEEP, 'Place to Sleep'),
    )
    type = models.IntegerField(choices=TYPES)
    coord_lat = models.FloatField()
    coord_long = models.FloatField()
    name = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField()

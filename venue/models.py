# coding=utf-8
from django.conf import settings
from django.db import models


class Place(models.Model):
    TYPE_RESTAURANT = 100
    TYPE_ACCOMMODATION = 200
    TYPES = (
        (TYPE_RESTAURANT, 'Place to Eat'),
        (TYPE_ACCOMMODATION, 'Place to Sleep'),
    )

    type = models.IntegerField(choices=TYPES)
    coord_lat = models.FloatField()
    coord_long = models.FloatField()
    name = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField()

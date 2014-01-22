# coding=utf-8
from django.conf import settings
from django.db import models


class Sponsor(models.Model):
    # Levels를 숫자로 한건 Ordering이 필요한 경우가 생길까 싶어서..
    LEVEL_KEYSTONE = 600
    LEVEL_DIAMOND = 500
    LEVEL_PLATINUM = 400
    LEVEL_GOLD = 300
    LEVEL_SILVER = 200
    LEVEL_PATRON = 100

    LEVELS = (
        (LEVEL_KEYSTONE, 'Keystone'),
        (LEVEL_DIAMOND, 'Diamond'),
        (LEVEL_PLATINUM, 'Platinum'),
        (LEVEL_GOLD, 'Gold'),
        (LEVEL_SILVER, 'Silver'),
        (LEVEL_PATRON, 'Patron'),
    )

    logo = models.ImageField(upload_to=settings.MEDIA_ROOT)
    level = models.IntegerField(choices=LEVELS)
    name = models.CharField(max_length=50)
    url = models.URLField()
    description = models.TextField()

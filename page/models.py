from django.db import models


class SiteConfig(models.Model):
    title = models.CharField(max_length=200, unique=True)
    swc = models.BooleanField(default=False)
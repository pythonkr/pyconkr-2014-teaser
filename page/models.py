from django.db import models


class SiteConfig(models.Model):
    title = models.CharField(max_length=200, unique=True)

    config_type = models.IntegerField(choices=(
        (1, u'Boolean'),
        (2, u'Integer'),
        (3, u'Character(200)'),
        (4, u'Text'),
        (5, u'Datetime'),
    ), default=1)

    config_boolean = models.NullBooleanField(blank=True, null=True)
    config_integer = models.IntegerField(blank=True, null=True)
    config_varchar = models.CharField(max_length=200, blank=True)
    config_text = models.TextField(blank=True)
    config_datetime = models.DateTimeField(blank=True, null=True)
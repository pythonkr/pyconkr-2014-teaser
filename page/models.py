from django.db import models
from datetime import datetime


class SiteConfigManager(models.Manager):
    def get_value(self, name, default=None):
        try:
            config = self.get(title=name)

            if config.config_type == SiteConfig.TYPE_BOOLEAN:
                return config.config_boolean
            elif config.config_type == SiteConfig.TYPE_INTEGER:
                return config.config_integer
            elif config.config_type == SiteConfig.TYPE_STRING:
                return config.config_varchar
            elif config.config_datetime == SiteConfig.TYPE_DATETIME:
                return config.config_datetime
        except SiteConfig.DoesNotExist as e:
            return default

    def set_value(self, name, value):
        config, created = self.get_or_create()

        config_type = type(value)
        if config_type == bool:
            config.config_type = SiteConfig.TYPE_BOOLEAN
            config.config_boolean = value
        elif config_type == int:
            config.config_type = SiteConfig.TYPE_INTEGER
            config.config_integer = value
        elif config_type == str or config_type == unicode:
            config.config_type = SiteConfig.TYPE_STRING
            config.config_varchar = value
        elif config_type == datetime:
            config.config_type = SiteConfig.TYPE_DATETIME
            config.config_varchar = value
        else:
            raise ValueError(u'Not Supported Type')

        config.save()


class SiteConfig(models.Model):
    TYPE_BOOLEAN = 1
    TYPE_INTEGER = 2
    TYPE_STRING = 3
    TYPE_DATETIME = 5

    objects = SiteConfigManager()

    title = models.CharField(max_length=200, unique=True)
    config_type = models.IntegerField(choices=(
        (TYPE_BOOLEAN, u'Boolean'),
        (TYPE_INTEGER, u'Integer'),
        (TYPE_STRING, u'String'),
        #(4, u'Text'),
        (TYPE_DATETIME, u'Datetime'),
    ), default=1)
    config_boolean = models.NullBooleanField(blank=True, null=True)
    config_integer = models.IntegerField(blank=True, null=True)
    config_varchar = models.CharField(max_length=200, blank=True)
    # config_text = models.TextField(blank=True)
    config_datetime = models.DateTimeField(blank=True, null=True)

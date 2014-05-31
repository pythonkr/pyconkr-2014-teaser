import hashlib
from django.core.cache import cache
from django.db import models


def cache_delete(fragment_name, var=''):
    args = hashlib.md5(var)
    cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
    cache.delete(cache_key)


class CacheDeleteMixin(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.template_cache_names:
            for name in self.template_cache_names:
                cache_delete(name)
        super(CacheDeleteMixin, self).save(*args, **kwargs)
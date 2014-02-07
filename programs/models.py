from django.db import models
from account.models import SiteUser


class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    speaker = models.ForeignKey(SiteUser)

    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)

    @property
    def duration(self):
        time_diff = self.end - self.start
        return time_diff.total_seconds()

    def __unicode__(self):
        return u'%s at. %s (%s)' % (self.title, self.start, seconds_to_string(self.duration))


def seconds_to_string(seconds):
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60

    return u'%sh %sm %ss' % (int(hours), int(minutes), int(seconds))
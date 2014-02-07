from django.db import models
from account.models import SiteUser
from programs.models import Program


class Registration(models.Model):
    user = models.ForeignKey(SiteUser)
    program = models.ForeignKey(Program)

    def __unicode__(self):
        return u'%s | %s' % (self.user, self.program)
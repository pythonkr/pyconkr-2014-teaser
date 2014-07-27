# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Program.room'
        db.add_column(u'pyconkr_program', 'room',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Program.room'
        db.delete_column(u'pyconkr_program', 'room')


    models = {
        u'pyconkr.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '2'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyconkr.Speaker']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pyconkr.siteconfiguration': {
            'Meta': {'object_name': 'SiteConfiguration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal_now': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'pyconkr.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'pyconkr.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pyconkr']
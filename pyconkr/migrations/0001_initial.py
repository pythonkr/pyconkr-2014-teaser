# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'pyconkr_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('intro', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=512)),
        ))
        db.send_create_signal(u'pyconkr', ['Speaker'])

        # Adding model 'Program'
        db.create_table(u'pyconkr_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyconkr.Speaker'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'pyconkr', ['Program'])

        # Adding model 'Sponsor'
        db.create_table(u'pyconkr_sponsor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=512)),
        ))
        db.send_create_signal(u'pyconkr', ['Sponsor'])

        # Adding model 'SiteConfiguration'
        db.create_table(u'pyconkr_siteconfiguration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proposal_now', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'pyconkr', ['SiteConfiguration'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'pyconkr_speaker')

        # Deleting model 'Program'
        db.delete_table(u'pyconkr_program')

        # Deleting model 'Sponsor'
        db.delete_table(u'pyconkr_sponsor')

        # Deleting model 'SiteConfiguration'
        db.delete_table(u'pyconkr_siteconfiguration')


    models = {
        u'pyconkr.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
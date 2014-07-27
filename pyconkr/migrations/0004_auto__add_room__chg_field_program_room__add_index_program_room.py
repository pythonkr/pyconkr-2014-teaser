# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'pyconkr_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'pyconkr', ['Room'])


        # Renaming column for 'Program.room' to match new field type.
        db.rename_column(u'pyconkr_program', 'room', 'room_id')
        # Changing field 'Program.room'
        db.alter_column(u'pyconkr_program', 'room_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pyconkr.Room']))
        # Adding index on 'Program', fields ['room']
        db.create_index(u'pyconkr_program', ['room_id'])


    def backwards(self, orm):
        # Removing index on 'Program', fields ['room']
        db.delete_index(u'pyconkr_program', ['room_id'])

        # Deleting model 'Room'
        db.delete_table(u'pyconkr_room')


        # Renaming column for 'Program.room' to match new field type.
        db.rename_column(u'pyconkr_program', 'room_id', 'room')
        # Changing field 'Program.room'
        db.alter_column(u'pyconkr_program', 'room', self.gf('django.db.models.fields.CharField')(max_length=2))

    models = {
        u'pyconkr.program': {
            'Meta': {'object_name': 'Program'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['pyconkr.Room']"}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pyconkr.Speaker']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pyconkr.room': {
            'Meta': {'object_name': 'Room'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'intro': ('django.db.models.fields.TextField', [], {'default': 'None'}),
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
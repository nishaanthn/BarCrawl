# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.twitter_id'
        db.add_column(u'location_location', 'twitter_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.fb_id'
        db.add_column(u'location_location', 'fb_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.fb_user_count'
        db.add_column(u'location_location', 'fb_user_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.twitter_id'
        db.delete_column(u'location_location', 'twitter_id')

        # Deleting field 'Location.fb_id'
        db.delete_column(u'location_location', 'fb_id')

        # Deleting field 'Location.fb_user_count'
        db.delete_column(u'location_location', 'fb_user_count')


    models = {
        u'location.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'fb_user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattitude_1': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lattitude_2': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lattitude_3': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lattitude_4': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lattitude_center': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_1': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_2': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_3': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_4': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_center': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tweeter_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['location']
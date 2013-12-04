# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'location_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('place_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('tweeter_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lattitude_1', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_1', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_2', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_2', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_3', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_3', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_4', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_4', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_center', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_center', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'location', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'location_location')


    models = {
        u'location.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'twitter_handle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['location']
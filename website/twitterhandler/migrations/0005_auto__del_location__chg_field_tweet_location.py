# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'twitterhandler_location')


        # Changing field 'Tweet.location'
        db.alter_column(u'twitterhandler_tweet', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location']))

    def backwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'twitterhandler_location', (
            ('longitude_4', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_1', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_3', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('longitude_2', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_4', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_1', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_2', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lattitude_3', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'twitterhandler', ['Location'])


        # Changing field 'Tweet.location'
        db.alter_column(u'twitterhandler_tweet', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitterhandler.Location']))

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
            'longitude_1': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_2': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_3': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude_4': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'user_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'twitterhandler.tweet': {
            'Meta': {'object_name': 'Tweet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']"}),
            'tweet_created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['twitterhandler']
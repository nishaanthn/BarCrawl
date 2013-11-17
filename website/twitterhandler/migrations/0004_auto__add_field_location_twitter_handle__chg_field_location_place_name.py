# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.twitter_handle'
        db.add_column(u'twitterhandler_location', 'twitter_handle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


        # Changing field 'Location.place_name'
        db.alter_column(u'twitterhandler_location', 'place_name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Location.twitter_handle'
        db.delete_column(u'twitterhandler_location', 'twitter_handle')


        # Changing field 'Location.place_name'
        db.alter_column(u'twitterhandler_location', 'place_name', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'twitterhandler.location': {
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
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['twitterhandler.Location']"}),
            'tweet_created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['twitterhandler']
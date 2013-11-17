# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'twitterhandler_user')

        # Deleting field 'Tweet.tweeter'
        db.delete_column(u'twitterhandler_tweet', 'tweeter_id')

        # Deleting field 'Location.longitude_threshold'
        db.delete_column(u'twitterhandler_location', 'longitude_threshold')

        # Deleting field 'Location.lattitude_threshold'
        db.delete_column(u'twitterhandler_location', 'lattitude_threshold')

        # Deleting field 'Location.lattitude_centroid'
        db.delete_column(u'twitterhandler_location', 'lattitude_centroid')

        # Deleting field 'Location.longitude_centroid'
        db.delete_column(u'twitterhandler_location', 'longitude_centroid')

        # Adding field 'Location.user_count'
        db.add_column(u'twitterhandler_location', 'user_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_1'
        db.add_column(u'twitterhandler_location', 'lattitude_1',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.longitude_1'
        db.add_column(u'twitterhandler_location', 'longitude_1',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_2'
        db.add_column(u'twitterhandler_location', 'lattitude_2',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.longitude_2'
        db.add_column(u'twitterhandler_location', 'longitude_2',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_3'
        db.add_column(u'twitterhandler_location', 'lattitude_3',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.longitude_3'
        db.add_column(u'twitterhandler_location', 'longitude_3',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_4'
        db.add_column(u'twitterhandler_location', 'lattitude_4',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.longitude_4'
        db.add_column(u'twitterhandler_location', 'longitude_4',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'twitterhandler_user', (
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_handle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_bio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user_followers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_following', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user_location', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'twitterhandler', ['User'])

        # Adding field 'Tweet.tweeter'
        db.add_column(u'twitterhandler_tweet', 'tweeter',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['twitterhandler.User']),
                      keep_default=False)

        # Adding field 'Location.longitude_threshold'
        db.add_column(u'twitterhandler_location', 'longitude_threshold',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_threshold'
        db.add_column(u'twitterhandler_location', 'lattitude_threshold',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.lattitude_centroid'
        db.add_column(u'twitterhandler_location', 'lattitude_centroid',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Location.longitude_centroid'
        db.add_column(u'twitterhandler_location', 'longitude_centroid',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Location.user_count'
        db.delete_column(u'twitterhandler_location', 'user_count')

        # Deleting field 'Location.lattitude_1'
        db.delete_column(u'twitterhandler_location', 'lattitude_1')

        # Deleting field 'Location.longitude_1'
        db.delete_column(u'twitterhandler_location', 'longitude_1')

        # Deleting field 'Location.lattitude_2'
        db.delete_column(u'twitterhandler_location', 'lattitude_2')

        # Deleting field 'Location.longitude_2'
        db.delete_column(u'twitterhandler_location', 'longitude_2')

        # Deleting field 'Location.lattitude_3'
        db.delete_column(u'twitterhandler_location', 'lattitude_3')

        # Deleting field 'Location.longitude_3'
        db.delete_column(u'twitterhandler_location', 'longitude_3')

        # Deleting field 'Location.lattitude_4'
        db.delete_column(u'twitterhandler_location', 'lattitude_4')

        # Deleting field 'Location.longitude_4'
        db.delete_column(u'twitterhandler_location', 'longitude_4')


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
            'place_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
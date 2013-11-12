# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'twitterhandler_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'twitterhandler', ['Location'])

        # Adding model 'User'
        db.create_table(u'twitterhandler_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_handle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_bio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user_followers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user_following', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'twitterhandler', ['User'])

        # Adding model 'Tweet'
        db.create_table(u'twitterhandler_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tweet_created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('tweeter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitterhandler.User'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitterhandler.Location'])),
        ))
        db.send_create_signal(u'twitterhandler', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'twitterhandler_location')

        # Deleting model 'User'
        db.delete_table(u'twitterhandler_user')

        # Deleting model 'Tweet'
        db.delete_table(u'twitterhandler_tweet')


    models = {
        u'twitterhandler.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'twitterhandler.tweet': {
            'Meta': {'object_name': 'Tweet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['twitterhandler.Location']"}),
            'tweet_created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tweeter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['twitterhandler.User']"})
        },
        u'twitterhandler.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_bio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_followers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_following': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_handle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['twitterhandler']
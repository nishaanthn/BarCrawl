from django.db import models

# Create your models here.


class Location(models.Model):
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)

class User(models.Model):
	user_id = models.CharField(max_length=50)
	user_handle = models.CharField(max_length=50)
	user_name = models.CharField(max_length=50)
	user_bio = models.CharField(max_length=200)
	user_followers = models.IntegerField(default=0)
	user_following = models.IntegerField(default=0)
	def __unicode__(self):
		return self.user_name

class Tweet(models.Model):
	tweet_id = models.CharField(max_length=50)
	tweet_text = models.CharField(max_length=200)
	tweet_created_at = models.DateTimeField('created at')
	tweeter = models.ForeignKey(User)
	location = models.ForeignKey(Location)
	def __unicode__(self):
		return self.tweet_id

from django.db import models
from location.models import Location

# Create your models here.


class Tweet(models.Model):
	tweet_id = models.CharField(max_length=50)
	tweet_text = models.CharField(max_length=200)
	tweet_created_at = models.DateTimeField('created at')
	location = models.ForeignKey(Location)
	def __unicode__(self):
		return self.tweet_id

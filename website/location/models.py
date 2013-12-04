from django.db import models

# Create your models here.

class Location(models.Model):
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	place_name = models.CharField(max_length=100)
	twitter_handle = models.CharField(max_length=30,default="",help_text="The twitter handle of the location.")
	twitter_id = models.CharField(max_length=50,default="",help_text="The twitter user id of the location")
	fb_id = models.CharField(max_length=50,default="",help_text="The facebook id of the location")
	tweeter_count = models.IntegerField(default=0,help_text="Number of twitter users at the location.")
	fb_user_count = models.IntegerField(default=0,help_text="Number of fb users at the location.")
	lattitude_1 = models.FloatField(default=0)
	longitude_1 = models.FloatField(default=0)
	lattitude_2 = models.FloatField(default=0)
	longitude_2 = models.FloatField(default=0)
	lattitude_3 = models.FloatField(default=0)
	longitude_3 = models.FloatField(default=0)
	lattitude_4 = models.FloatField(default=0)
	longitude_4 = models.FloatField(default=0)
	lattitude_center = models.FloatField(default=0)
	longitude_center = models.FloatField(default=0)
	def __unicode__(self):
		return self.place_name

from django.contrib import admin
from twitterhandler.models import Tweet,Location

	
class NewTweet(admin.ModelAdmin):
	search_fields = ['user_name']

admin.site.register(Tweet, NewTweet)
admin.site.register(Location)
# Register your models here.

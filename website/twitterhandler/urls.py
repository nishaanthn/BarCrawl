from django.conf.urls import patterns, url

from twitterhandler import views

urlpatterns = patterns('',
	url(r'^$', views.locationIndex, name='index'),
	#url(r'^(?P<user_id>\d+)/$', views.userDetails, name='userDetails'),
	url(r'^(?P<loc_id>\d+)/$', views.locationDetails, name='locationDetails'),
	#url(r'^(?P<tweet_id>\d+)/$', views.tweetDetails, name='tweetDetails'),
	
)

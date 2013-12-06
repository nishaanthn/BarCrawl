from django.conf.urls import patterns, url, include
from django.contrib import admin
from twitterhandler import views

urlpatterns = patterns('',
	url(r'^$', views.homePage, name='homePage'),
	#url(r'^(?P<user_id>\d+)/$', views.userDetails, name='userDetails'),
	url(r'^(?P<loc_id>\d+)/$', views.locationDetails, name='locationDetails'),
	url(r'^bars/', views.locationList, name='locationList'),
	url(r'^about/', views.aboutUs, name='aboutUs'),
	url(r'^contact/', views.contactUs, name='contactUs'),
	url('^admin/', include(admin.site.urls)),
	#url(r'^(?P<tweet_id>\d+)/$', views.tweetDetails, name='tweetDetails'),
	
)

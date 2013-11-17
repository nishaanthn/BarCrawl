from django.conf.urls import patterns, url

from location import views

urlpatterns = patterns('',
	url(r'^$', views.locationIndex, name="index"),
	url(r'^(?P<loc_id>\d+)/$', views.locationDetails, name="detail"),
)


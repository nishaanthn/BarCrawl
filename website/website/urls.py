from django.conf.urls import patterns, include, url

from django.contrib import admin
import twitterhandler
import location
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^twitterhandler/', include('twitterhandler.urls', namespace="twitterhandler")),
    url(r'^location/', include('location.urls', namespace="location")),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', twitterhandler.views.homePage, name='home'),
)

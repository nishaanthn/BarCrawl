from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from location.models import Location
from twitterhandler.models import Tweet

def homePage(request):
	latest_loc_list = Location.objects.order_by('-tweeter_count')[:5]
	context = { 'latest_loc_list': latest_loc_list}
	return render(request, 'twitterhandler/index3.html', context)

def locationIndex(request):
	latest_loc_list = Location.objects.order_by('-place_name')[:5]
	context = { 'latest_loc_list': latest_loc_list}
	return render(request, 'twitterhandler/index.html', context)
	
def locationDetails(request, loc_id):
	try:
		location = Location.objects.get(pk=loc_id)
	except Location.DoesNotExist:
		raise Http404
	return render(request, 'twitterhandler/detail.html', {'location':location})

def locationList(request):
	return render(request, 'twitterhandler/bars.html')
	
def contactUs(request):
	return render(request, 'twitterhandler/contact_us.html')

def aboutUs(request):
	return render(request, 'twitterhandler/who_we_are.html')
	
	
	
def tweetDetails(request, tweet_id):
	try:
		tweet = Tweet.objects.get(pk=tweet_id)
	except Tweet.DoesNotExist:
		raise Http404
	return render(request, 'twitterhandler/detail.html', {'tweet':tweet})
	

# Create your views here.

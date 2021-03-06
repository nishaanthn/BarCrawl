from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from location.models import Location
from twitterhandler.models import Tweet

def homePage(request):
	latest_loc_list = Location.objects.order_by('-tweeter_count')[:5]
	loc_list = Location.objects.order_by('-tweeter_count')
	context = { 'latest_loc_list': latest_loc_list, 'loc_list': loc_list}
	return render(request, 'twitterhandler/index3.html', context)

def locationIndex(request):
	latest_loc_list = Location.objects.order_by('-place_name')[:5]
	context = { 'latest_loc_list': latest_loc_list}
	return render(request, 'twitterhandler/index.html', context)
	
def locationDetails(request, loc_id):
	try:
		locations = Location.objects.get(pk=loc_id)
		tweets = Tweet.objects.filter(location__twitter_handle=locations.twitter_handle)
	except Location.DoesNotExist:
		raise Http404
	return render(request, 'twitterhandler/detail.html', {'location':locations, 'tweets':tweets})

def locationList(request):
	loc_list = Location.objects.order_by('-tweeter_count')
	context = { 'loc_list': loc_list}
	return render(request, 'twitterhandler/allbars.html', context)
	
	
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

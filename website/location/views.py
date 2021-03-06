from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from location.models import Location

def homePage(request):
	latest_loc_list = Location.objects.order_by('-place_name')
	context = { 'latest_loc_list': latest_loc_list}
	return render(request, 'location/index.html', context)

def locationIndex(request):
	loc_list = Location.objects.order_by('-place_name')[:10]
	context = { 'loc_list': loc_list}
	return render(request, 'location/index.html', context)
	
	

def locationDetails(request, loc_id):
	try:
		location = Location.objects.get(pk=loc_id)
	except Location.DoesNotExist:
		raise Http404
	return render(request, 'location/detail.html', {'location':location})



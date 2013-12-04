from BarCrawlClasses import Bar as Bar
from location.models import Location
import json
import os

# --- Global Variable
bars = []				# Temporary storage, Change as necessary


def loadAllBarData(fileName):
	with open('locationfixtures.json') as datafile:
		jdata = json.load(datafile)
		for bar in jdata:
			print bar
			l = Location(country = "USA",city = "College Station",place_name = bar['name'],twitter_handle = bar['twtter_handle'],twitter_id = bar['twitter_id'],fb_id = bar['fb_id'],lattitude_1 = bar['lattitude_1'],longitude_1 = bar['longitude_1'],lattitude_2 = bar['lattitude_2'],longitude_2 = bar['longitude_2'],lattitude_3 = bar['lattitude_3'],longitude_3 = bar['longitude_3'],lattitude_4 = bar['lattitude_4'],longitude_4 = bar['longitude_4'],lattitude_center = bar['lattitude_center'],longitude_center = bar['longitude_center'])
			l.save()


if __name__ == "__main__":
	loadAllBarData("locationfixtures.json")
from location.models import Location
from twitterhandler.models import Tweet as BarTweet
import json
import os


directoryName = os.getcwd()

# loop through the files in the data folder
for myfile in os.listdir(directoryName):
	print myfile
	with open(myfile, 'r') as datafile:
		tweetData = json.load(datafile)
		for tweet in tweetData:
			print tweet
			#l = Location(country = "USA",city = "College Station",place_name = bar['name'],twitter_handle = bar['twtter_handle'],twitter_id = bar['twitter_id'],fb_id = bar['fb_id'],lattitude_1 = bar['lattitude_1'],longitude_1 = bar['longitude_1'],lattitude_2 = bar['lattitude_2'],longitude_2 = bar['longitude_2'],lattitude_3 = bar['lattitude_3'],longitude_3 = bar['longitude_3'],lattitude_4 = bar['lattitude_4'],longitude_4 = bar['longitude_4'],lattitude_center = bar['lattitude_center'],longitude_center = bar['longitude_center'])
			#l.save()
			locName = os.path.splitext(myfile)[0]
			t = BarTweet(tweet_id = tweet['id'] , tweet_text = tweet['text'], tweet_created_at = tweet['created_at'], location = locName)
			t.save()

import tweepy
import json
import re
import os
import thread
from stemming import porter2
from BarCrawlClasses import Tweet as Tweet
from BarCrawlClasses import Bar as Bar
from CSVreader import loadAllBarData
import Tweet_Crawler_Functions as helperFunctions


# --- Global Variables
bars = []
barHandles = []
barIDs = []
tweetsToClassify = []
generalBarGoerTweets = []

homeLat = 30.587457
homeLon = -96.342547
		

''' ^^^^^^^^   Handles Data Received from Each Twitter Stream. ^^^^^^^^^^ '''
class TweetStreamListener(tweepy.StreamListener):
 	
    def __init__(self, _streamID, _api):
    	""" --- Stream ID is used to determine where to send the collected Tweets in on_status --- """
    	self.api = _api	
    	super(tweepy.StreamListener, self).__init__()
    	self.streamID = _streamID


    def on_status(self, status):
        """ --- When a Status/Tweet is Captured, It Comes Here --- """

        # --- Create Tweet Obeject From Pieces of the Tweet We Need
    	lat, lon = status.geo["coordinates"] if status.geo else ('', '')

    	# --- FOR TESTING ONLY REMOVE SOON ----
    	print "hashtags = " 
    	print status.entities['hashtags']

    	# --- Save the Relevant Information From the HashTag  (All We Need is the Tag Text)
    	tagList = []
    	for tag in status.entities['hashtags']:
    		tagList.append(tag['text'])

    	tempTweet = Tweet(status.id, status.created_at, status.text, status.entities['user_mentions'], tagList, lat, lon)
        	

        # --- Tweet is Collected With the Handle Stream
        if self.streamID == "handle":
        	helperFunctions.storeTweet(tempTweet, bars)

        # --- Tweet is Collected With the Location Stream: Classify Tweet Relative to Specific Bar OR Just a Happy NorthGater
        elif self.streamID == "location":
        	helperFunctions.classifyTweet(tempTweet, bars, generalBarGoerTweets)		
 			#print "lat = " + str(lat) + '\t' + "lon = " + str(lon) + '\n'

        return True


 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True 			# Return True To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True 			# Return True To continue listening



class TweetCrawler():
	
	def __init__(self):
		
		# --- Information to connect to Twitter
		self.consumer_key = 'Fqa4EEvWUfBmoPMCd5m2A'
		self.consumer_secret = 'B2LVBSfnUzcviVsnf2vmAspKNfFpAghoh7fPRHXYs8o'
		self.access_key = '192438534-Xw3SRwiJPfLUcdT5w80dTIq6MsVRrVJduHYWbJuo'
		self.access_secret = 'ZOZJmQn5ahre4N4OjardbTUhVFmKSXzIidSpqoaRnHc'
		
		# --- Authorize Twitter information
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_key, self.access_secret)
		self.api = tweepy.API(self.auth)

		# --- Stream / Listener Variables
		self.handleListener = TweetStreamListener("handle", self.api)
		self.locationListener = TweetStreamListener("location", self.api)
	
	
	def CollectTweetsByHandle(self):
		self.handleStream = tweepy.Stream(auth = self.auth, listener = self.handleListener)
		self.handleStream.filter(follow = barIDs, track = barHandles)


	def CollectTweetsByLocation(self, _lattitude, _longitude, _radius, _units):
		searchLocation = str(_lattitude) + "," + str(_longitude) + "," + str(_radius) + str(_units)

		self.locationStream = tweepy.Stream(self.auth, self.locationListener)
		self.locationStream.filter(follow = None, locations=[-102.33,31.84,-102.28,31.91])


if __name__ == "__main__":
	
	homeLat = 30.587457
	homeLon = -96.342547


	# --- Load the Bar Data From File (Will Change this to Load from DataBase)
	loadAllBarData("BarData.csv", bars)
	helperFunctions.loadStreamFiterLists(bars, barHandles, barIDs)

	tweetCrawler = TweetCrawler()
	tweetCrawler.CollectTweetsByHandle()
	#tweetCrawler.CollectTweetsByLocation(homeLat, homeLon , 0.1 , "mi")
	






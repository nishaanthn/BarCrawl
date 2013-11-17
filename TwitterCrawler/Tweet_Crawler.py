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

count = 0

# --- Global Variables
bars = []
barHandles = []
barIDs = []
tweetsToClassify = []
specificBarTweets = {}  			#  ---> {Bar TwitterHandle : [tweet_1, ..., tweet_n] } 
generalBarGoerTweets = []

		

''' ^^^^^^^^   Handles Data Received from Each Twitter Stream. ^^^^^^^^^^ '''
class TweetStreamListener(tweepy.StreamListener):
 	
    def __init__(self, _streamID, _api):
    	""" --- Stream ID is used to determine where to send the collected Tweets in on_status --- """
    	self.api = _api	
    	super(tweepy.StreamListener, self).__init__()
    	self.streamID = _streamID


    def on_status(self, status):
        """ --- When a Status/Tweet is Captured, It Comes Here --- """

        # --- Tweet is Collected With the Handle Stream
        if self.streamID == "handle":

        	# --- Create Tweet Obeject From Pieces of the Tweet We Need
        	lat, lon = status.geo["coordinates"] if status.geo else ('', '')
        	tempTweet = Tweet(status.id, status.created_at, status.text, lat, lon, status.entities['user_mentions'])
        	

        	# --- Determine Which Bar(s) Were Mentioned
        	barsMentioned = helperFunctions.determine_Bars_Mentioned(status.entities['user_mentions'], bars)

        	# --- Add Tweet to specificBarTweets Object
        	for barName in barsMentioned:
        		# will need thread lock here
        		specificBarTweets[barName].append(tempTweet)

        	# --- Print the Tweets Collected ( *** Testing Purposes Only *** )
        	helperFunctions.printCollectedTweets(specificBarTweets)



        # --- Tweet is Collected With the Location Stream
        elif self.streamID == "location":
        	
        	# --- Classify Tweet: Relative to Specific Bar OR Just a Happy NorthGater
        	hi = 1
 		
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


	def CollectTweetsByLocation(self, _lattitude, _longitude, _radius):
		searchLocation = str(_lattitude) + "," + str(_longitude) + "," + str(_radius)

		self.locationStream = Stream(self.auth, self.locationListener)
		self.locationStream.filter(follow = None, geocode = searchLocation)

		
	def loadTwitterHandleList(self, fileName):
		""" --- Reads the Bar Data from the File --- """
		inputFile = open(fileName)

		for line in inputFile:
			# --- Split the Line at the Comma
			lineContents = line.split(',')

			# --- Save Contents of Line
			barHandle = lineContents[0].strip()
			barID = lineContents[1].strip()

			# --- Store barHandle 
			specificBarTweets[barHandle] = []
			barHandles.append( ("@" + str(barHandle)) )
			
			# --- Store barIDs
			barIDs.append(barID)


if __name__ == "__main__":
	tweetCrawler = TweetCrawler()
	#tweetCrawler.loadTwitterHandleList("TwitterHandleNames.txt")
	#tweetCrawler.CollectTweetsByHandle()
	#print specificBarTweets
	loadAllBarData("BarData.csv", bars)






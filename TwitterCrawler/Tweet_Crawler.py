import tweepy
import json
import re
import os
import thread
from stemming import porter2
from BarCrawlClasses import Tweet as Tweet
from BarCrawlClasses import Bar as Bar

count = 0

# --- Global Variables
bars = []
barHandles = []
barIDs = []
tweetsToClassify = []
specificBarTweets = {}  			#  ---> {Bar TwitterHandle : [tweet_1, ..., tweet_n] } 
generalBarGoerTweets = []


def printCollectedTweets():
	print " ---- specificBarTweets --- \n"
	for bar in specificBarTweets:
		print "BAR NAME: " + str(bar)
		for tweet in specificBarTweets[bar]:
			tweet.printTweet()
		

class TweetStreamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''
 	
    def __init__(self, _streamID, _api):
    	""" --- Stream ID is used to determine where to send the collected Tweets in on_status --- """
    	self.api = _api	
    	super(tweepy.StreamListener, self).__init__()
    	self.streamID = _streamID
    	

    def determine_Bars_Mentioned(self, userMentions):
    	""" --- Check All Users Mentioned in Tweet to Find Bar(s) That Were Mentioned ---"""
    	tweetHandleNames = []

    	for userMentioned in userMentions:
    		if userMentioned['screen_name'] in specificBarTweets:
				tweetHandleNames.append(userMentioned['screen_name'])

    	return tweetHandleNames


    def on_status(self, status):
        """ --- When a Status/Tweet is Captured, It Comes Here --- """

        if self.streamID == "handle":

        	# --- Create Tweet Obeject From Pieces of the Tweet We Need
        	lat, lon = status.geo["coordinates"] if status.geo else ('', '')
        	tempTweet = Tweet(status.id, status.created_at, status.text, lat, lon, status.entities['user_mentions'])
        	

        	# --- Determine Which Bar(s) Were Mentioned
        	barsMentioned = self.determine_Bars_Mentioned(status.entities['user_mentions'])

        	# --- Add Tweet to specificBarTweets Object
        	for barName in barsMentioned:
        		# will need thread lock here
        		specificBarTweets[barName].append(tempTweet)


        	print "---specificBarTweets--- \n"
        	for bar in specificBarTweets:
        		print "BAR NAME: " + str(bar)
        		for tweet in specificBarTweets[bar]:
        			tweet.printTweet()




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


	def loadAllBarData(self, fileName):
		inputFile = open(fileName)

		for line in inputFile:
			# --- Split the Line at the Comma
			lineContents = line.split(',')

			# --- Remove WhiteSpace From Each lineContent
			for piece in lineContents:
				piece = piece.strip()

			# --- Save the Contents of the Line
			barName = lineContents[0]
			barTwitterHandle = lineContents[1]
			barFBid = lineContents[2]
			#bar4SquareID = lineContents[3]
			
			barCornerLocs = []
			swCorner = (float(lineContents[4]), float(lineContents[5]))
			nwCorner = (float(lineContents[6]), float(lineContents[7]))
			neCorner = (float(lineContents[8]), float(lineContents[9]))
			seCorner = (float(lineContents[10]), float(lineContents[11]))

			barCornerLocs.append(swCorner)
			barCornerLocs.append(nwCorner)
			barCornerLocs.append(neCorner)
			barCornerLocs.append(seCorner)

			barCenter = (float(lineContents[12]), float(lineContents[13]))


			bar = Bar(barName, barCenter, barCornerLocs, barTwitterHandle, barFBid, "USA", "College Station")
			bars.append(bar)

		# --- Printing Bar Data (for testing)
		for bar in bars:
			bar.printBarData()

if __name__ == "__main__":
	tweetCrawler = TweetCrawler()
	#tweetCrawler.loadTwitterHandleList("TwitterHandleNames.txt")
	#tweetCrawler.CollectTweetsByHandle()
	#print specificBarTweets
	tweetCrawler.loadAllBarData("BarData.csv")






import tweepy
import json
import re
import os
from stemming import porter2
import BarCrawlClasses
from datetime import datetime

class TweetCollector():
	
	
	def __init__(self):
		self.consumer_key = 'Fqa4EEvWUfBmoPMCd5m2A'
		self.consumer_secret = 'B2LVBSfnUzcviVsnf2vmAspKNfFpAghoh7fPRHXYs8o'
		self.access_key = '192438534-Xw3SRwiJPfLUcdT5w80dTIq6MsVRrVJduHYWbJuo'
		self.access_secret = 'ZOZJmQn5ahre4N4OjardbTUhVFmKSXzIidSpqoaRnHc'
		
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_key, self.access_secret)
		self.api = tweepy.API(self.auth)
		
		self.queries = []
		
	
	def CollectTweets(self, query):
		
		# Create File info for tweets
		fileName = query.replace(" ", "") + ".txt"
		"""
		if os.path.exists("Documents"):
			outPutFile = open(os.path.join("Documents", fileName.lower()), 'w+')
		else:
			os.makedirs("Documents")
			outPutFile = open(os.path.join("Documents", fileName.lower()), 'w+')
		"""
		
		if os.path.exists("BarCrawlData"):
			outPutFile = open(os.path.join("BarCrawlData", fileName.lower()), 'w+')
		else:
			os.makedirs("BarCrawlData")
			outPutFile = open(os.path.join("BarCrawlData", fileName.lower()), 'w+')
		
		tweetText = ""
		
		i = 0
		for tweet in tweepy.Cursor(self.api.search,q=query, result_type="recent", include_entities=True, lang="en").items():
		#for tweet in tweepy.Cursor(self.api.search,geocode="30.618737,-96.347245,.1mi", count=20, result_type="recent", include_entities=True, lang="en").items():
			
			
			''' -- Older code , may be useful later 
			#outPutFile.write(str(tweet.text.encode('utf-8')) + '\n')
			#lat, lon = tweet.geo["coordinates"] if tweet.geo else ('', '')
			#outPutFile.write(str(tweet.text.encode('utf-8')) + '\t' + "Coordinates: (" + str(lat) + " , " + str(lon) + ")" + '\n')
			'''
			
			# Check date info
			dateCreated = datetime.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S')
			oldestDate = datetime(2013, 11, 7)
			
			if (dateCreated > oldestDate):
				outPutFile.write("{\"created_at\":\"" +  str(tweet.created_at) + "\"," + "\"id\": \"" + str(tweet.id) + "\"," + "\"text\":\"" + str(tweet.text.encode('utf-8')).replace('\n', '') + "\"}\n")
			else:
				print "This date is too old! "
				print dateCreated
				break
			#print(tweet.geo)
			print tweet.created_at
			
			
	
	def read_query_list(self, fileName):
		inputFile = open(fileName)
		
		for line in inputFile:
			for query in line.split(','):
				self.queries.append(query.strip())
			
		
	
	def send_querys(self):
		#Loop through all querys and send that them to the tweet collector
		i = 0
		for query in self.queries:
			print query
			self.CollectTweets(query)
	
if __name__ == "__main__":
	tweetCollector = TweetCollector()
	#tweetCollector.read_query_list("queryList.txt")
	tweetCollector.read_query_list("ProjectQueryList.txt")
	tweetCollector.send_querys()
import tweepy
import json
import re
import os
import thread
from stemming import porter2
import BarCrawlClasses

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
		
		# --- Variables
		self.queries = []
		self.tweetsToClassify = []
		self.generalBarGoerTweets[]
		self.specificBarTweets[]  #---> {Bar TwitterHandle : tweet } 
		
	
	
	def CollectTweetsByHandle(self, twitterHandle):
		
		






class Tweet():
	
	def __init__(self, _tweetId, _createdAt, _text, _lat, _lon, _userMentions):
		
		# --- Important info needed from each collected tweet
		self.tweetID = _tweetID
		self.createdAt = _createdAt
		self.text = _text
		self.lattitude = _lat
		self.longitude = _lon
		self.userMentions = _userMentions
	

class Bar():
	def __init__(self, _name, _twitterHandle, _latLoc, _lonLoc):
		
		# --- Initialize the hand-gather bar information
		self.name = _name
		self.twitterHandle = _twitterHandle
		self.latLoc = _latLoc
		self.lonLoc = _lonLoc
		
		self.tweetList = []
		




class Tweet():
	
	def __init__(self, _tweetID, _createdAt, _text, _userMentions, _hashTags, _lat = None , _lon = None ):
		
		# --- Important info needed from each collected tweet
		self.tweetID = _tweetID
		self.createdAt = _createdAt
		self.text = _text
		self.lattitude = _lat
		self.longitude = _lon
		self.userMentions = _userMentions
		self.hashTags = _hashTags

	def printTweet(self):
		print " \t tweetID: " + str(self.tweetID) + "\n"
		print " \t createdAt: " + str(self.createdAt) + "\n"
		print " \t text: " + str(self.text) + "\n"
		print " \t lat: " + str(self.lattitude) + "\n"
		print " \t lon: " + str(self.longitude) + "\n"
		print " \t userMentions: " + str(self.userMentions) + "\n"
		print " \t hashTags: " + str(self.hashTags) + "\n\n"
		

class Bar():
	def __init__(self, _name, _centerOfBarLoc, _barCorners, _twitterHandle = "", _twitterID = "" , _barFBid = "" , _country = "", _city = ""):
		
		# --- Initialize the hand-gather bar information
		self.country = _country
		self.city = _city
		self.name = _name
		self.twitterHandle = _twitterHandle
		self.twitterID = _twitterID
		self.FBid = _barFBid
		self.centerOfBarLoc = _centerOfBarLoc
		self.barCorners = _barCorners
		
		self.tweetList = []
	

	def printBarData(self):
		print " ********************************************************"
		print " \t name: " + str(self.name) + "\n"
		print " \t twitterHandle: " + str(self.twitterHandle) + "\n"
		print " \t twitterID nt: " + str(self.twitterID) + "\n"
		print " \t FBid: " + str(self.FBid) + "\n"
		print " \t SW Bar Corner: " + str(self.barCorners[0]) + "\n"
		print " \t NW Bar Corner: " + str(self.barCorners[1]) + "\n"
		print " \t NE Bar Corner: " + str(self.barCorners[2]) + "\n"
		print " \t SE Bar Corner: " + str(self.barCorners[3]) + "\n"
		print " \t Center of Bar: " + str(self.centerOfBarLoc) + "\n"
		print " ******************************************************** \n "

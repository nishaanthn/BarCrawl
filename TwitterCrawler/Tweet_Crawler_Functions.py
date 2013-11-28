import tweepy
import math
from BarCrawlClasses import Tweet as Tweet
from BarCrawlClasses import Bar as Bar

''' ---------------- Functions For Testing/ Printing -------------------- '''
def printCollectedTweets(barList):
	print " ---- barList --- \n"
	for bar in barList:
		#bar.printBarData()
		print "Bar Name: " + str(bar.name) 
		print "---------------------------"
		for tweet in bar.tweetList:
			tweet.printTweet()


def printList(givenList, objectName):
	print "Now Printing " + str(objectName)
	print "--------------------------------"
	for listObj in givenList:
		print str(objectName) + " = " + str(id) + '\n'

''' ----------------- End Printing Functions ---------------------------- '''


def loadStreamFiterLists(barList, barHandleList, barIDlist):
	""" --- Get the Handles AND ID of Each Bar (Used for the Streams) --- """
	for bar in barList:
		if bar.twitterHandle != "":
			barHandleList.append("@" + str(bar.twitterHandle))

		if bar.twitterID != "":
			barIDlist.append(bar.twitterID)



def storeTweet(tweet, bars):
	""" --- Store Tweet Picked Up by the Listener ---"""

	# --- Determine Which Bar(s) Were Mentioned
	barMentioned = determine_Bars_Mentioned(tweet.userMentions ,  bars)

	# --- Add Tweet to Targeted Bar TweetList
	if barMentioned != "NO_BARS_FOUND":
		for bar in bars:
			if bar.twitterHandle == barMentioned:
				# --- Will need thread lock here
				bar.tweetList.append(tweet)
				print "Stored a tweet!" + str(barMentioned)
				break


def determine_Bars_Mentioned(userMentions, bars):
	""" --- Check All Users Mentioned in Tweet to Find Bar(s) That Were Mentioned ---"""
	"""                As of now, only save the first mentioned bar 				 """

	for userMentioned in userMentions:
		for bar in bars:
			if bar.twitterHandle == userMentioned['screen_name']:
				return (userMentioned['screen_name'])

	return "NO_BARS_FOUND"


def findBarInHashTag(tweet, bars):
	""" --- Check All HashTags in Tweet to Find Bar(s) That Were Tagged ---"""

	for tag in tweet.hashTags:
		for bar in bars:
			barName = bar.name.replace(" ", "")

			# maybe check if the hastag contains the bar name 
			if bar.twitterHandle.lower() == tag.lower() or barName.lower() == tag.lower():
				bar.tweetList.append(tweet)
				print "BAR WAS TAGGED!" + str()
				return True

	return False


def geoDistance(loc1, loc2):
	""" -------- Find the GeoDistance Between to Points on the Earth ---------- """
	""" 	Source: http://www.johndcook.com/python_longitude_latitude.html 	"""


	# --- Guarantee that Both Locations Are Not Blank.  If so, return 100 (large distance away from bar)
	if loc1[0] == "" or loc1[1] == "" or loc2[0] == "" or loc2[1] == "":
		return 100				

	R = 3963
	lat1 = float(loc1[0])			
	long1 = float(loc1[1])
	lat2 = float(loc1[0])
	long2 = float(loc1[1])

	# --- phi = 90 - latitude
	phi1 = math.radians(90.0 - lat1)
	phi2 = math.radians(90.0 - lat2)
	    
	# --- theta = longitude
	theta1 = math.radians(long1)
	theta2 = math.radians(long2)


	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
	       math.cos(phi1)*math.cos(phi2))
	arc = math.acos( round(cos, 10) )

	return arc * R


def findClosestBars(k_closest , tweetLocation, barList):
	""" --- Finds the K Closest Bars to the Given Tweet Location ---  """

	closestBars = []

	for bar in barList:

		# --- If closestBars is Empty or Less then K
		if not closestBars or  len(closestBars) < k_closest:
			closestBars.append((bar , geoDistance(tweetLocation , bar.centerOfBarLoc)))
		else:
			# --- Sort the List from Closest to Farthest Bar Away
			closestBars.sort(key= lambda tup: tup[1])

			# --- Loop Through the List and Find Closer Bars (if any)
			for idx, closeBar in enumerate(closestBars):
				distToBar = geoDistance(tweetLocation , bar.centerOfBarLoc)

				# --- If the Dist to Current Bar is Less, Pop Largest Bar off End of List
				if distToBar < closeBar[1]:
					closestBars.pop()
					closestBars.insert(idx , (bar , distToBar) )


	# --- Make ClosestBars Just a List of Bars (Remove the geoDistance from the pair)
	for idx,bar in enumerate(closestBars):
		closestBars[idx] = bar[0]

	return closestBars


def insideBarCoordinates(x , y, barPoly):
	""" ----- Determine If the Given Point Falls Inside the Polygon of the Bar Coordinates ---- """
	""" 				Source: http://geospatialpython.com/2011/01/point-in-polygon.html		"""

	n = len(barPoly)
	inside = False

	p1x,p1y = barPoly[0]
	for i in range(n+1):
	    p2x,p2y = barPoly[i % n]
	    if y > min(p1y,p2y):
        	if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y

	return inside


def tweetFromInsideBar(tweet, closestBarstoTweet):
	""" --- Returns Wether or Not the Tweet Happened Inside A Bar ---  """

	for bar in closestBarstoTweet:
		if insideBarCoordinates(tweet.lattitude, tweet.longitude, bar.barCorners):
			bar.tweetList.append(tweet)
			return True

	return False




def classifyTweet(tweet, bars, generalBarGoers):
	""" --- Classify Tweets Collected by Location: They are Either Specific to a Bar or a General Bar Goer Tweet ----- """

	# --- Check for Bar(s) in Tweet Hashtags
	barInHastag = findBarInHashTag(tweet , bars)

	# --- No Bars Were Tagged, So Classify by Location
	if barInHastag is False:
		tweetLoc = (tweet.lattitude , tweet.longitude)

		# --- Was Tweet Sent From Inside Bar GeoCoordinates?
		closestBars = findClosestBars(3, tweetLoc, bars)
		tweetedFromInsideBar = tweetFromInsideBar(tweet , closestBars)

		# --- If Not, Its Just a General BarGoer Tweet
		if tweetedFromInsideBar is False:
			generalBarGoers.append(tweet)





import tweepy, json, time
import pyspeedtest

st = pyspeedtest.SpeedTest()

def auth():
	try:
		with open('secrets.json', 'r') as f:
			data = json.load(f)
			CKEY = data["auth0"]["CKEY"]
			CSECRET = data["auth0"]["CSECRET"]
			AKEY = data["auth0" ]["ATOKEN"]
			ASECRET = data["auth0"]["ASECRET"]
			auth = tweepy.OAuthHandler(CKEY, CSECRET)
			auth.set_access_token(AKEY, ASECRET)
			return tweepy.API(auth)
	except:
		print("Authentication failed.")
	
def getInternetInfo():
	return (int(st.download() / 1000000), int(st.upload() / 1000000))

def formatForTweet(stats):
	return ("Download: " + str(stats[0]) + " Mbps\nUpload: " + 
		str(stats[1]) + " Mbps")


def writeToFile(stats):
	currentTime = time.strftime("%m-%d-%Y_%H:%M:%S")
	fileName = currentTime

	currentTime += "\n" + formatForTweet(stats) 

	with open("data/dat", 'a') as f:
		f.write(fileName + " " + str(getInternetInfo())[1:-1] + "\n")
	return currentTime

def scan(download = 500, upload = 5, debug = False):
	stats = getInternetInfo()
	if debug:
		print("Download: " + str(stats[0]) + " Mbps\nUpload: " + 
		str(stats[1]) + " Mbps\n" + "Ping: " + str(stats[2]) + " ms")

	writeToFile(stats)
	key = auth()
	
	currDownload = stats[0]
	currUpload = stats[1]
	if currDownload < download:
		tweet = "Hey Charter, I pay for " + str(download) + "Mbps. I'm only getting " + str(currDownload) + " Mbps. What's up with that? :("
	key.update_status(tweet)









if __name__ == '__main__':
	scan()
"""run <sudo pip install twython> before use. Gather Twitter app key, app secret, oauth token, and token secret and set them to environment
variables using: <export APP_KEY= 'your key'>, <export APP_SECRET='your secret'>, <export OAUTH_TOKEN='your token'>,
 and <export OAUTH_TOKEN_SECRET='your token secret'> in the command line"""

def twitterTopicGrab(topic=None):
	from twython import Twython
	from index import havenSentiment 
	import os

	APP_KEY =  os.environ.get('twitterKey')
	APP_SECRET = os.environ.get('twitterSecret')
	OAUTH_TOKEN = os.environ.get('twitterToken')
	OAUTH_TOKEN_SECRET = os.environ.get('twitterTokenSecret')

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	twitter.verify_credentials()
	if topic != None:
		relevantTweets = twitter.search(q=topic, result_type='popular')
	tweets = []
	for x in relevantTweets['statuses']:
		if 'text' in x:
			tweets.append(x['text'])

	return havenSentiment(tweets)
def twitterUserGrab(user=None):
	from twython import Twython
	from index import havenSentiment
	import os

	APP_KEY =  os.environ.get('twitterKey')
	APP_SECRET = os.environ.get('twitterSecret')
	OAUTH_TOKEN = os.environ.get('twitterToken')
	OAUTH_TOKEN_SECRET = os.environ.get('twitterTokenSecret')

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	twitter.verify_credentials()
	
	if user != None:
		user_timeline = twitter.get_user_timeline(screen_name=user)

	tweets = []
	for x in user_timeline:
		if 'text' in x:
			tweets.append(x['text'])
	return havenSentiment(tweets)
if __name__ == '__main__':
	print twitterTopicGrab("python")
	print twitterUserGrab("kanyewest")


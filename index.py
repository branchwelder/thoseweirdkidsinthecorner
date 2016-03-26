"""Run <pip install git+https://github.com/HPE-Haven-OnDemand/havenondemand-python> in the command console before use."""
def havenSentiment(text):	
	"""Takes a string as an input and runs it through the Haven API to gather sentiment analysis and returns it"""
	from havenondemand.hodindex import HODClient
	import os
	key = os.environ.get('havenAPI')
	client = HODClient(apikey=key, apiversiondefault=1)
	data = {'text': text}
	r = client.post('analyzesentiment', data)
	sentiment = r.json()['aggregate']['sentiment']
	score = r.json()['aggregate']['score']
	# return text + " | " + sentiment + " | " + str(score)
	return score




if __name__ == "__main__":
	from twitterGrab import twitterUserGrab
	from twitterGrab import twitterTopicGrab
	print havenSentiment(twitterTopicGrab("python"))
	print havenSentiment(twitterUserGrab("kanyewest"))
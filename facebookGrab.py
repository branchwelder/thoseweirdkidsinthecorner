
def facebookGrab(profile):
	"""Get an access token from facebook and run: <export facebookAcessToken = 'your token'> in the command line."""
	import facebook
	import requests
	import os
	from index import havenSentiment
	import json

	results = []
	access_token = os.environ.get('facebookAcessToken')
	# access_token = 'CAABqy6QtDmwBAIlvxqiSRog7TtqWzLDL8RRtabQ4Sjaic6XWZCbcY099wIeaVDXbEsJJZCfZB56hpBBumTx95JPqSEfKryKNY6ZBzHMQZCn0e47Wws1sZA6aZA18Sluv0iAqDwVCXZBZAqskdCdFRIl2wJRYzrIm6rnexIW10ivGBTkXgaIZCcXZBFVdR6F09PYZAOBlZB2XhHT0Kn0MZApekKZCfRT'
	user = profile

	graph = facebook.GraphAPI(access_token)

	# app_id = '117422865321580' # Obtained from https://developers.facebook.com/
	# app_secret = '7e977218d4526ea175991deeeaefc589' # Obtained from https://developers.facebook.com/
	app_id = os.environ.get('facebookAppId')
	app_secret = os.environ.get('facebookAppSecret')


	# Extend the expiration time of a valid OAuth access token.
	extendedAccessToken = graph.extend_access_token(app_id, app_secret)
	# graph = facebook.GraphAPI(extendedAccessToken)

	profile = graph.get_object(user)
	posts = graph.get_connections(profile['id'], 'posts')

	# graph = facebook.GraphAPI(user_short_lived_token_from_client)



	# Wrap this block in a while loop so we can keep paginating requests until
	# finished.
	for i in range(5):
	    try:
	        # Perform some action on each post in the collection we receive from
	        # Facebook.
	        [results.append(post['message']) for post in posts['data']]
	        # Attempt to make a request to the next page of data, if it exists.
	        posts = requests.get(posts['paging']['next']).json()
	    except KeyError:
	        # When there are no more pages (['paging']['next']), break from the
	        # loop and end the script.
	        break
	return havenSentiment(json.dumps(results))

if __name__ == '__main__':
	print facebookGrab('BillGates')

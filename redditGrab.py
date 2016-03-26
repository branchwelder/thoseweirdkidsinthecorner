def posts_about(about, limit=100, subreddit='all'):
	"""Uses a Reddit wrapper to access the top posts on a particular topic and the resulting comments.
	It then runs sentiment analysis on those comments and averages them. This function returns one number
	indicating the subjectivity of the comments."""
	import praw
	import json
	from index import havenSentiment
	r = praw.Reddit(user_agent='CTW')
	posts = r.get_subreddit(subreddit).get_hot(limit=limit)
	ps = []
	for post in posts:
		if about.lower() in str(post).lower():
			ps.append(post)
	

	processed = []
	for i in range(len(ps)):
		processed.append(str(ps[i]))
	res = ' '.join(processed)
	# res = json.dumps(res)
	return havenSentiment(res)

if __name__ == '__main__':
	print posts_about('trump')
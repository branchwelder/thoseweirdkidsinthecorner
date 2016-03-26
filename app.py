from flask import Flask, render_template, request, jsonify
from redditGrab import posts_about
from twitterGrab import twitterTopicGrab, twitterUserGrab
from facebookGrab import facebookGrab
from fractal import draw_snowflake
import time
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/topic_results', methods=['POST'])
def get_results():
	print "(HIDSIHSDFIHSDFIHSDFIH)"
	topic = request.form["topic"].encode('utf-8')
	source = request.form["source"].encode('utf-8')
	tu = request.form["tu"].encode('utf-8')

	if source == "facebook":
		print "facebook"
		sentiment = facebookGrab(topic)
	elif (source == "twitter" and tu == "user"):
		print "twitter user"
		sentiment = twitterUserGrab(topic)
	elif (source == "twitter" and tu == "topic"):
		print "twitter topic"
		sentiment = twitterTopicGrab(topic)
	elif source == "reddit":
		print "reddit"
		sentiment = posts_about(topic)
	else:
		sentiment = 0


	draw_snowflake(sentiment)
	
	time.sleep(1)

	return jsonify({"hi":"helellelle"})

if __name__ == '__main__':
	app.run()

from redditGrab import posts_about
from twitterGrab import twitterTopicGrab, twitterUserGrab
from facebookGrab import facebookGrab
from fractal import draw_snowflake

def do(source, topic, tu):
    # if source == "facebook":
    # 	print "facebook"
    # 	sentiment = facebookGrab(topic)
    # elif (source == "twitter" and tu == "user"):
    # 	print "twitter user"
    # 	sentiment = twitterUserGrab(topic)
    # elif (source == "twitter" and tu == "topic"):
    # 	print "twitter topic"
    # 	sentiment = twitterTopicGrab(topic)
    # elif source == "reddit":
    # 	print "reddit"
    # 	sentiment = posts_about(topic)
    # else:
    # 	sentiment = 0

    sentiment = 0

    draw_snowflake(sentiment)

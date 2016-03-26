from redditGrab import posts_about
from twitterGrab import twitterTopicGrab, twitterUserGrab
from facebookGrab import facebookGrab
from fractal import draw_snowflake

def do(source=None, topic=None, tu=None, sentiment=None):
    if sentiment != None:
            draw_snowflake(sentiment)
    else:
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


if __name__=='__main__':
    print do("facebook", "trump")
    print do("twitter", "trump", "user")
    print do("twitter", "trump", "topic")
    print do("reddit", "trump")
    print do (sentiment=(2.00-0.21))

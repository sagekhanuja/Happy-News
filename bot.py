import tweepy
import time
from textblob import TextBlob
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy.api
from tweepy import Cursor
import re

consumer_key = 'insert token here'
consumer_secret = 'insert token here'

access_token = 'insert token here'
access_token_secret = 'insert token here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)




class TwitterBot:

    def __init__(self, news_twitterhandle): #news_twitterhandle is the @ name of the twitter entity
        global news_twitter
        self.news_twitterhandle = news_twitterhandle
        news_twitter = self.news_twitterhandle

    def find_user_history(self):
        tweethistory = api.user_timeline(screen_name = news_twitter, count = 1, include_rts = False)
        for status in tweethistory:
            (status._json)
        tweet_text = status._json['text']
        global clean_tweet
        global id
        clean_tweet = str(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet_text).split()))
        print(clean_tweet)
        id = int(status._json['id_str'])
        print(clean_tweet)
        

    def sentiment_analysis(self):
        opinion = TextBlob(clean_tweet)
        global sentiment
        sentiment = opinion.sentiment.polarity
        print("The polarity for this tweet is " + str(sentiment))

    def retweet(self):
        if sentiment >= .01:
            print("Statement detected as positive")
            print("Retweeted------------------->>>>\n")
        try:
            api.retweet(id)

        except tweepy.TweepError as e: 
            print("error detected; reason:\n")
            print(e.reason)
        else:
             print("------------------------Statement detected is detected as negative----------------------\n")


def main(): 
    
    
    #declaring the npr object and iterating through the functions in the retweet class
    npr = TwitterBot("NPR")
    npr.find_user_history()
    npr.sentiment_analysis()
    npr.retweet()
    

    nytimes = TwitterBot("nytimes")
    nytimes.find_user_history()
    nytimes.sentiment_analysis()
    nytimes.retweet()

    #declaring the npr object and iterating through the functions in the retweet class
    
    washpost = TwitterBot("washingtonpost")
    washpost.find_user_history()
    washpost.sentiment_analysis()
    washpost.retweet()


    BBC = TwitterBot("BBCWorld")
    BBC.find_user_history()
    BBC.sentiment_analysis()
    BBC.retweet()
    
starttime=time.time()


#setting a time loop, the main() function will execute every 15 minutes. 
while True:
  time.sleep(900.0 - ((time.time() - starttime) % 900.0))
  main()



    
    



# -*- coding: utf-8 -*-

import tweepy
from tweepy.api import API
import re
import glob
import time

from unidecode import unidecode


numfiles = len(glob.glob('tweets/*'))

API_KEY = 'x'
API_SECRET = 'x'
ACCESS_TOKEN = 'x'
ACCESS_TOKEN_SECRET = 'x'
key = tweepy.OAuthHandler(API_KEY, API_SECRET)
key.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

aantaltweets = 0
global aantaltweets


class Stream2Screen(tweepy.StreamListener):

    
    def __init__(self, api=None):
        self.api = api or API()
        self.n = 0
        self.m = 1000

    def on_status(self, status):
        #print status
        global aantaltweets
        filenaam = "tweets/tweet" + str(self.n + numfiles) + ".txt"
        aantaltweets += 1
        #print status.text.encode('utf8') #+ 
        #print self.n
        tweet = re.sub(r'[^\x00-\x7F]+',' ', status.text)
        tempval = tweet.decode('utf8')
        tweet = unidecode(tempval)

        text_file = open(filenaam, "w")
        text_file.write(tweet)
        text_file.close()


        self.n = self.n+1
        if self.n < self.m: return True
        else:
            #print 'tweets = '+str(self.n)
            return False



for i in range(1,500):
	#Pak er 500, soms loopt het script vast. vermoedelijk door non-ascii codes.
    stream = tweepy.streaming.Stream(key, Stream2Screen())

    stream.filter(track=['de'], languages=['nl'])
    print i,"iteraties.",aantaltweets,"tweets"
    time.sleep(10) #for good measure 10 seconden wachten tussen calls. Kan geen kwaad.

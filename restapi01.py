#-*- coding: utf-8 -*-

#first, authenticate with your application credentials
from TwitterAPI import TwitterAPI
import json
from TwitterAPI import TwitterRestPager 
import conf
import os
import datetime

consumer_key = conf.consumer_key
consumer_secret = conf.consumer_secret
access_token_key = conf.access_token_key
access_token_secret = conf.access_token_secret

SEARCH_TERM={'영화','보고 왔습니다','보고 왔어요'}

api = TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret) 

startTime = datetime.datetime.now()
priorHour=startTime.hour
if not os.path.exists("./data/"+startTime.strftime("%Y-%m-%d")):
    os.makedirs("./data/"+startTime.strftime("%Y-%m-%d"))
path = "./data/"+startTime.strftime("%Y-%m-%d")+"/"+startTime.strftime("%Y-%m-%d-%H")+".dat"

f = open(path, 'w',encoding='utf8')



#with open('outputs_restapi01.dat', 'w',encoding='utf8') as f:
while(1):
  r =TwitterRestPager(api, 'search/tweets', {'q':SEARCH_TERM})
  for item in r.get_iterator(wait=5, new_tweets=True):
      currentTime = datetime.datetime.now()
      currentHour = currentTime.hour
      if priorHour != currentHour:
           f.close()
           if not os.path.exists("./data/"+currentTime.strftime("%Y-%m-%d")):
               os.makedirs("./data/"+currentTime.strftime("%Y-%m-%d"))
           path = "./data/"+currentTime.strftime("%Y-%m-%d")+"/"+currentTime.strftime("%Y-%m-%d-%H")+".dat"
           f = open(path, "w", encoding='utf8')
           priorHour = currentHour
      f.write(str(item))
      if 'message' in item and item['code'] == 88:
        break


#stream tweets from New York City //print some tweets in the location // continuously
"""r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
for item in r:
        print(item)"""

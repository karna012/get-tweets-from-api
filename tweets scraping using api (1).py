#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tweepy


# In[20]:


import tweepy
import datetime
import pytz
import pandas as pd

# Authenticate with Twitter API using API keys
api_key_tw = 'use your api key'
api_key_tw_secret = 'use your api secret key'
access_token = 'use your access token'
access_token_secret = 'use your access secret key'

auth = tweepy.OAuthHandler(api_key_tw, api_key_tw_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Search for tweets with a given keyword
keyword = 'roshtein'

#get tweets of last 7 days from now
current_date = datetime.datetime.now()
tweets = api.search_tweets(keyword, lang='en', count=10, since_id=(current_date - datetime.timedelta(days=7)).strftime('%Y-%m-%d'), until=current_date.strftime('%Y-%m-%d'))

# Print the tweets and their dates
tweets_with_dates = []
for tweet in tweets:
    tweet_date = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
    tweet_text = tweet.text
    tweets_with_dates.append([tweet_date, tweet_text])
    print(tweet_date, tweet_text)

# Create a DataFrame with the tweets and their dates
df = pd.DataFrame(tweets_with_dates, columns=['date', 'tweet'])
df


# In[21]:


# Print the retweets and their dates
retweets_with_dates = []
for tweet in tweets:
    if hasattr(tweet, 'retweeted_status'):
        tweet_date = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
        tweet_text = tweet.text
        retweets_with_dates.append([tweet_date, tweet_text])
        print(tweet_date, tweet_text)

# Create a DataFrame with the retweets and their dates
df1 = pd.DataFrame(retweets_with_dates, columns=['date', 'retweet'])
df1


# In[ ]:





# predict_stocks_with_tweets.py
# By: Mark Torres
# This script contains functions for predicting stock returns using tweets about the stock
# 
# Input: 
#	1. twitter_credentials: text file that contains Twitter credentials
#	2. start_date: the start date of the scraping
#	3. end_date: the end date of the scraping
#	4. search terms: list of search terms (e.g., ticker symbol, stock name)
# Output: 
#	1. Price predictions (end-of-day) 
#	2. R-squared of model
#
#

# import necessary libraries
import tweepy
import csv
import json
import numpy as np
import pandas as pd
import nltk
import textblob
from textblob import TextBlob
from nltk.corpus import stopwords
import re
import string
import datetime
from datetime import date
import yfinance as yf
from pandas_datareader import data as pdr
import sklearn
import matplotlib.pyplot as plt
import sys 
import os

# for web scraping
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import ast
from urllib.request import Request, urlopen

########## Pt 0: Setup ###############

### Take command line arguments
credentials_file = sys.argv[1]
start_date = sys.argv[2]
end_date = sys.argv[3]
search_terms  = [sys.argv[4:]]

# load credentials from text file
with open(credentials_file) as f:
    credentials = f.read().splitlines()
    
# assign keys
consumer_key = credentials[0]
consumer_secret = credentials[1]
access_token = credentials[2]
access_token_secret = credentials[3]

# now, we authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

########## Pt 1: Scrape and clean tweets ###############

# store tweets in an array. We also need to keep track of the dates when the tweets were posted

tweets = []
tweet_dates = []

# use a for loop to iterate through words to search:
for search_word in search_query:
    
    # get tweets
    tweets_to_add = tweepy.Cursor(api.search, 
                                 q = search_word, 
                                 start = start_date, 
                                 end = end_date).items()
    
    # for each of the tweets, get the text (since we care only about the text for sentiment analysis)
    
    tweet_text = []
    tweet_dates_loop = []
    
    for tweet in tweets_to_add: 
        tweet_text.append(tweet.text) # extract the text of the tweet
        tweet_dates_loop.append(tweet.created_at) # extract the date and time when the tweet was created
        
    # add to list of tweets
    tweets.append(tweet_text)
    tweet_dates.append(tweet_dates_loop)

# Now that we have the tweets, we need to clean them so that they can be used in the project. 
# To do so, we'll extract punctuation and eliminate common stopwords (e.g., "and", "or", "else").

# download stopwords
nltk.download('stopwords')

# create new tweets array and dates array, both of which append two rows of list into one row
tweets_updated = np.array(tweets[0] + tweets[1]) 
dates_updated = np.array(tweet_dates[0] + tweet_dates[1]) 

# use pandas dataframe to vectorize the operation
tweets_df = pd.DataFrame(tweets_updated, columns = ["tweet"])

# get set of stopwords
stopword_set = set(stopwords.words("english"))

# convert to lower case, split
tweets_df["tweet"] = tweets_df["tweet"].str.lower()

# split words
tweets_df["split_tweets"] = tweets_df["tweet"].str.split()

# remove stopwords using apply with list comprehension, to vectorize the operation
tweets_df["no_stopwords"] = tweets_df["split_tweets"].apply(lambda tweet: [word for word in tweet if word not in stopword_set])

# keep only the words
def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = [''.join(c for c in s if c not in string.punctuation) for s in text]
        #text = text.replace(punctuation, '')
    return text

tweets_df["only_words"] = tweets_df["no_stopwords"].apply(remove_punctuations)

# let's get the cleaned tweets 
cleaned_tweets = tweets_df["only_words"].str.join(" ")

########## Pt 2: Perform Sentiment Analysis ###############

# use Textblob to get sentiments

assigned_sentiments = []

for tweet in cleaned_tweets:

    # get textblob object
    text_sentiment = TextBlob(tweet)
    
    # get sentiment
    sentiment_score = text_sentiment.sentiment.polarity
    
    # append to list of sentimentsa
    assigned_sentiments.append(sentiment_score)

# create pandas dataframe with the date and the sentiment
tweet_sentiments_dates = pd.DataFrame(list(zip(dates_updated, assigned_sentiments)), 
                                      columns = ["Timestamp", "Sentiment Score"])

# create a new column that has only the date (no info on time)
tweet_sentiments_dates["Date"] = [d.date() for d in tweet_sentiments_dates["Timestamp"]]

# do a group-by and a summarize to calculate the average sentiment score, by date
average_sentiment_byDay = tweet_sentiments_dates.groupby('Date').agg({'Sentiment Score': 'mean'})

########## Pt 3: Scrape Prices ###############

# use yfinance and override pandas datareader's functionality for get_data_yahoo
yf.pdr_override()

# get data about Tesla stock
tesla_stock = pdr.get_data_yahoo("TSLA", start = start_date, end = end_date)

# get time stamp of each date
tesla_stock["time_stamp"] = [datetime.datetime.utcfromtimestamp(x/1e9) for x in tesla_stock.index.values.astype(date)]

# set index
tesla_stock.set_index("time_stamp")

# merge the sentiment data with the price data
merged_df = pd.concat([average_sentiment_byDay, tesla_stock], sort = True)

########## Pt 4: Make predictions ###############

# split the data into observations
X = merged_df[['Sentiment Score']]
y = merged_df[['Close']]

# do train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train linear regression model
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# make predictions
y_pred = regressor.predict(X_test)

# get r-2
r_2 = sklearn.metrics.r2_score(y_test, y_pred)

# let's return what the actual prices were, as well as the results:
print("Here are some actual prices during this time period: ")
print(y_test)

print("Here's what the model predicted would be the prices during this time period: ")
print(y_pred)

# now let's see what the r-2 is:
print("The r-squared of the model is: " + str(r_2))


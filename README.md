# Using Tweets to Predict Stock Prices

First attempt at predicting stock prices using sentiment analysis of tweets. 

### Motivation for project

### Implementation

### Current challenges

#### Transforming Python script into functioning web app

At the moment, I am developing my knowledge of web development so I can create a functioning web app that implements this Python script in the backend. Once that code is completed, it will be uploaded as well. 

#### Adding functionality to the Python script
This current Python script works, but still requires additional functionality to be a useful app. In particular, I plan on implementing the following features in the future:

##### 1. Filtering by positive/negative tweets. 

In my script, I analyze the sentiment of a tweet. It could be interesting to look at, for example, whether positive tweets have a stronger effect on the price than negative tweets. Implementing this functionality in the Python script is not difficult, since it would include an additional line that filters the tweets by their sentiment score. A previous version of the Python script had this functionality but it is currently being eliminated until I can implement a user interface to synchronize with it, which I am currently working on. 

##### 2. Including appropriate weights for certain tweets. 

Presumably, certain tweets (e.g., for Tesla, a tweet by Elon Musk) would hold more weight than others (e.g., a tweet about Tesla from a consumer). Currently, my implementation weighs all tweets equally. In reality, certain tweets would clearly carry more weight than other tweets. Therefore, a future implementation could possibly weigh tweets depending on the person who tweeted the message. My first approach is to take advantage of Twitter's "Verified" feature, which gives a special "Verified" status to certain users who are particularly well-known. Perhaps it is possible to weigh tweets depending on whether a user is "Verified". However, this approach runs into its own problems as well (e.g., a celebrity with no affiliation to Tesla could still tweet about it, and their tweet wouldn't have much influence on the price itself). 

### Where I see this project going eventually


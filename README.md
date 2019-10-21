# Using Tweets to Predict Stock Prices

This repository summarizes my progress in creating a web app that uses tweets to predict stock prices. It is still very much a work in progress, but it's a project that I enjoy doing and gives me a great opportunity to improve my programming and data science skills.

### 1. Motivation for project:

I know that in the future, I would like to work in the space of data science. I enjoy the intersection of statistics and research and I see data science as a framework that combines qualitative skills (e.g., asking good questions, interpreting results, etc.) with quantitative skills (e.g., knowing the latest ML models, interpreting summary statistics, programming, etc.). While taking a few online courses to supplement my statistics coursework at Yale, I've been tinkering with side projects to improve my skillset. However, this project is my first major attempt at implementing a long-term independent project that brings together all the skills that I've developed. I wanted a project that would use Twitter text data since, due to my background in psychology, I'm interested in how people interact with each other. After knowing that I would use Twitter data, I picked stock prediction as the problem I wanted to tackle, since it's a problem that I know I would not be able to solve with a simple data science project, which means that there will always be room to improve on my work. I see this project as a way to bring together my skills in a very engaging way that allows me to create a tangible end product.  

### 2. Implementation:

Currently, I see this project as taking two steps:

##### 1. Python backend:

##### 2. Web frontend (HTML/CSS/JS):



### 3. Current challenges: 

#### Transforming Python script into functioning web app

At the moment, I am developing my knowledge of web development so I can create a functioning web app that implements this Python script in the backend. This involves creating the functionality in small, iterative steps, as I progress in my online web development course. Once that code is completed, it will be uploaded as well. 

#### Adding functionality to the Python script
This current Python script works, but still requires additional functionality to be a useful app. In particular, I plan on implementing the following features in the future (in addition to others):

##### 1. Filtering by positive/negative tweets. 

In my script, I analyze the sentiment of a tweet. It could be interesting to look at, for example, whether positive tweets have a stronger effect on the price than negative tweets. Implementing this functionality in the Python script is not difficult, since it would include an additional line that filters the tweets by their sentiment score. A previous version of the Python script had this functionality but it is currently being eliminated until I can implement a user interface to synchronize with it, which I am currently working on. 

##### 2. Including appropriate weights for certain tweets. 

Presumably, certain tweets (e.g., for Tesla, a tweet by Elon Musk) would hold more weight than others (e.g., a tweet about Tesla from a consumer). Currently, my implementation weighs all tweets equally. In reality, certain tweets would clearly carry more weight than other tweets. Therefore, a future implementation could possibly weigh tweets depending on the person who tweeted the message. My first approach is to take advantage of Twitter's "Verified" feature, which gives a special "Verified" status to certain users who are particularly well-known. Perhaps it is possible to weigh tweets depending on whether a user is "Verified". However, this approach runs into its own problems as well (e.g., a celebrity with no affiliation to Tesla could still tweet about it, and their tweet wouldn't have much influence on the price itself). 

##### 3. Using additional predictive variables in the model. 

Currently, I am predicting stock prices purely based on sentiment scores. If our goal is to provide the best predictions possible, then including additional variables would improve the predictive power of the model. Moreover, using more variables would allow for more complex models to be used. I am still trying to figure out what additional variables would be informative in this type of model. I currently believe that using economic indices as well as prices of similar stocks would serve as good controls. A future version of this implementation would scrape this information and include it in the model. 

### Where I see this project going eventually

Eventually, my goal is 


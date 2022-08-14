# **Stock market future priceprediction model**
![Comparison Between Models in the Fashion MNIST dataset](https://cdn1.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/analytics-circle-blue-512.png)

## Problem Statement:
By use of various tools and techniques we have to create a website or application on which we can analyze data for various stock markets, not just the Indian Stock Market. And also can upload custom MS Excel sheets of data and analyze the data and also can download the data in form of an Excel sheet. There should also be predictions based on data that how the market will perform in the future. 

# Table of Contents
* [process](https://github.com/Akashkunwar/IIT-Madras-Datahacks#Process)
* [Tools useda](https://github.com/Akashkunwar/IIT-Madras-Datahacks#Tools_used)
* [Performance](https://github.com/Akashkunwar/IIT-Madras-Datahacks#Peformance)
* [Usage in Market](https://github.com/Akashkunwar/IIT-Madras-Datahacks#Usage_in_market)


## Process

1. First, we download data or scrape data from finance which is the website of yahoo so that we can make changes in data and use it to train the model on top of it.
2. After it, we do some pre-processions and train the TensorFlow Keras model on top of it which takes approx more than 20 minutes.
3. In the end here comes the deployment part and we deployed our model by using streamlit in this we integrated HTML with python to work in real-time to work in user input.

## Tools Used

1. `Yfinance : ` From here we used to scrape data and used it in my model.
2. `Python : ` I mainly used python as a main language and used tensorflow keras on top of it to train the model.
3. `Streamlit : ` We used streamlit to deploy our Machine learning model to give us ease to select stock and describe, visualize and train the model and give the final result.

## Performance

* `Traning data` : 
 We got Train RSME as `301.7` which is very food for our model by the way training RSME is always less.
 * `Testing data` : 
 We get Testing RSME as `1325.4` which is low from the training data bit it is also very impressive considering our model.
 

## Usage in market

*   `Indian Market : `
 I have tested this model on Indian stocks like LIC, Reliance, Zomato, and IRCTS and it works perfectly fine here.

*   `US Market : `
 I have also tested this model on Indian stocks like apple, google, tesla and Microsoft and in this also it works perfectly fine here.

*   `Any Market : `
 So, we can assume that this model will perform and give a very good result in most of the stock markets.

*   `Conclusion : `
 Most of the stock market around the globe works in very similar manner and behave similarly.

## Links
* [Youtube video link](https://youtu.be/UupM2qIrpZc)
* [Pitch deck link](https://www.canva.com/design/DAFJNYBIu5c/eKIMjsM6s8t9mNsNB3CqMg/edit?utm_content=DAFJNYBIu5c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## About
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)



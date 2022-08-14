# **Stock market future priceprediction model**
![Comparison Between Models in the Fashion MNIST dataset](https://cdn1.iconfinder.com/data/icons/social-messaging-ui-color-shapes/128/analytics-circle-blue-512.png)

## Problem Statement:
By use of various tools and techniques we have to create a website or application on which we can analyze data for various stock markets, not just the Indian Stock Market. And also can upload custom MS Excel sheets of data and analyze the data and also can download the data in form of an Excel sheet. There should also be predictions based on data that how the market will perform in the future. 

# Table of Contents

* [The Concept](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#the-concept)
* [The Data](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#the-data)
* [Data Cleaning](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#the-cleaning)
* [EDA (Exploratory data analysis)](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#EDA-(Exploratory-data-analysis))
* [Encoding](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#Encoding)
* [Scaling](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#Scaling)
* [ML Model Deployment](https://github.com/Akashkunwar/Dscourses/tree/main/Guvi/Project/Chennai%20House%20Price%20Prediction#ML-Model-Deployment)


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


## About
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/aakashkunwar/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

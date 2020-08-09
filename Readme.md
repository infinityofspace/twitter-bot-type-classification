# Twitter bot type classification

Comparison of different machine learning models and different Twitter bot types.

---

### Table of Contents

1. [About](#about)
2. [Getting started](#getting-started)
    1. [Generate new dataset](#generate-new-dataset)
    2. [Calculate features](#calculate-features)
    3. [Webpage](#webpage)
3. [Feature categories](#feature-categories)
    1. [User](#user)
    2. [Tweet](#tweet)
    3. [User and Tweet based](#user-and-tweet-based)
4. [Results](#results)
    1. [Bot types](#bot-types)
    2. [ML models](#ml-models)
5. [TODOs](#todos)
6. [Third party notices](#third-party-notices)
7. [License](#license)

---

### About

> Note: This project is intended for academic research context

[Twitter](https://twitter.com) is a microblogging service on which not only human users are active.
So there are Twitter accounts that publish helpful information on Twitter.
An example would be a Twitter account that publishes the current weather or earthquake information as a tweet.
But there are also malicious Twitter accounts that spread spam or false information.
All this Twitter accounts are called bots.
It is important not only to make a distinction between bot and human, but also to look at the different bot types in a very differentiated way.
This is important, because the different bot types not only have very different characteristics, but bad bots must be separated from the good ones, so that appropriate actions can be taken against bad bots.

This project compares 6 different machine learning models for the classification of 10 different Twitter bot types.
The classification results were also compared with those of Botometer.
[Botometer](https://botometer.iuni.iu.edu) is a service that offers a classification of a human or bot.

The project also offers the possibility to easily create new Twitter datasets and to calculate features for the classification.

### Getting started

#### Installation

Clone the project:

```commandline
git clone https://github.com/infinityofspace/twitter-bot-type-classification.git
```

Change the current working directory:

```commandline
cd twitter-bot-type-classification
```

Install the project:

```commandline
python3 setup.py install
```

#### Generate new dataset

Generate a new Twitter dataset the `twitter-bot-generate` command.
For example this command gets the last 200 Tweets for each username in the bot_usernames.csv file and saves the users into the users.cb and the tweets into tweets.db.

```commandline
twitter-bot-generate <api-app-key> <api-app-secret> -u users.db -t tweets.db -l 200 -f bot_usernames.csv --usernames
```

> Note: You have to obtain your own app key and secret. There is a [guide](https://developer.twitter.com/en/docs/basics/getting-started) on how to obtain them.

All available options:

```commandline
usage: twitter-bot-generate [-h] [-u [USERS]] [-t [TWEETS]] [-l LIMIT] [-f [FILE]] [--usernames] [--csv] [--skip-header] api_keys api_keys

Generate Twitter dataset of tweet and user data.

positional arguments:
  api_keys              Twitter API App key and secret

optional arguments:
  -h, --help            show this help message and exit
  -u [USERS], --users [USERS]
                        Output file for user data
  -t [TWEETS], --tweets [TWEETS]
                        Output file for tweet data
  -l LIMIT, --limit LIMIT
                        Limit greater or equal 1 of tweets loaded for each user. Use -1 to get all available tweets. Default value is 200
  -f [FILE], --file [FILE]
                        Input file to be used
  --usernames           The input file contains usernames instead user ids
  --csv                 Store the file as csv file instead sqlite
  --skip-header         Skip the first line of the input file
```

#### Calculate features

Generate a new Twitter dataset the `twitter-bot-features command.
For example this command calculate the features for each user and its last 50 tweets and saves them into the file features.npz.

```commandline
twitter-bot-features -u users.db -t tweets.db -l 50 -f features.npz
```

All available options:

```commandline
usage: twitter-bot-features [-h] -u USERS -t TWEETS [-l LIMIT] -f FILE [-w WORKER] [--csv] [--skip-header]

Calculate tweet and user features from database.

optional arguments:
  -h, --help            show this help message and exit
  -u USERS, --users USERS
                        Input file of user data
  -t TWEETS, --tweets TWEETS
                        Input file of tweet data
  -l LIMIT, --limit LIMIT
                        Limit of tweets to use for each user. If -1 all available tweets are used
  -f FILE, --file FILE  Output fle to save the calculated features
  -w WORKER, --worker WORKER
                        Number of worker to use for the feature calculation
  --csv                 The provided input files are csv files. Default is sqlite database
  --skip-header         Skip the first line of the csv input file
```

### Feature categories

The features used are divided into 3 basic categories User, Tweet and combination of both.
In total there are 60 User features and 171 Tweet features.
The combination of User und Tweet features and additional features in category three are 234 features in total.

#### User

The following features are calculated exclusively from account metadata.

| Temporal |
| :---: |
| account age |
| quotient of account age and #Tweet |

| Metadata |
| :---: |
| #user mentions in profile description |
| #URLs in profile description |
| profile description contains own username |
| profile description contains name |
| profile description length |
| #numbers in profile description |
| #Emojis in profile description |
| profile description contains "Bot" |
| username length |
| username contains name |
| #number in username |
| username structure |
| private account |
| verified |
| account location provided |
| username contains "Bot" |
| name length |
| #numbers in name |
| #Emojis in name |
| name contains "Bot" |
| profile URL to other service |
| profile URL domain contains username |
| profile URL domain contains name |
| profile URL path contains username |
| profile URL domain contains name |
| default profile picture |
| default background |
| #Tweets |
| #follower |
| #friends |
| #lists |
| #likes |
| quotient of #follower and #friends |
| quotient of #Tweets and #likes |

Abbreviations:
- \#: quantity
- M: arithmetic mean
- S: standard deviation
- MAX: maximum
- MIN: minimum

#### Tweet

The following features are calculated exclusively from tweet metadata.

| Temporal |
| :---: |
| Tweet interval (M/S) |

| Metadata |
| :---: |
| Tweet likes (M/S/MIN/MAX) |
| Tweet Retweets (M/S/MIN/MAX) |
| #self-replies |
| #different countries |
| country with most tweets |
| #Tweet sources |
| most used Tweet source |
| proportion of Retweets |
| proportion of responses |
| #countries with withheld tweets (M, MAX) |
| #different tweet coordinate groups |
| most used Tweet coordinate group |
| #replies to different users |
| #pictures (M/S) |
| #videos (M/S) |
| #gifs (M/S) |

| Content |
| :---: |
| Tweet Text length (not trimmed) (M/S/MIN/MAX)|
| #hashtags (M/S/MIN/MAX) |
| hashtag length (M/MIN/MAX)  |
| text length without Emojis/URLs (M/S/MIN/MAX) |
| #user mentions (M/S/MIN/MAX) |
| #sentences (M/S) |
| #words (M/S) |
| #Emojis (M/S/MIN/MAX) |
| #Tweets only with Emojis |
| #different Tweet languages |
| most used Tweet language |
| #Tweets with pagination |
| text similarity of own tweets (M/S) |
| text similarity of the Retweets (M/S) |
| #URLs (M/S) |
| #Tweets only contains URLs |

Abbreviations:
- \#: quantity
- M: arithmetic mean
- S: standard deviation
- MAX: maximum
- MIN: minimum

#### User and Tweet based

This feature category contains all user and tweet features and the following additional features:

| |
| :---: |
| Quotient of #URLs in the Tweet without and with the same domain as username |
| Quotient of #URLs in the Tweet without and with the same domain as profile URL |
| Quotient of #URLs in the Tweet and #shortened-URls |

Abbreviations:
- \#: quantity

### Results

This project was tested with a dataset of 10 different bot types.
The different bot types are explained in detail under the [bot types](bot-types) section.
Results can be found in the subfolder [results](results) as Jupyter Notebook.
The classification performance of each ML model is considered separately for each feature category.
This allows an evaluation of the classification performance of different data, because each feature category requires a different amount of data and calculation time to achieve good results.
In addition, as the distribution of bot types was not balanced in the data set, the oversampling methods SMOTE and ADASYN were tested for better classification performance.
A summarized and visualized overview of the classification performance of the different ML models can be viewed in the [overview file](results/clf_overview.ipynb).

Twitter has very [strict guidelines](https://developer.twitter.com/en/developer-terms/agreement-and-policy) for the use and publication of Twitter user data.
For this reason I cannot publish the complete raw data set used for this project.
In addition, all data and Jupyter notebooks that are directly related to the raw dataset set are not available in this repo.

#### Bot types

The following bot types were used for the classification comparison.

| bot type | intent | imitate human behavior | description |
| :---: |:---:| :---:| :---:|
| human | none | none | normal human user |
| feed | + | - | send news or links to new news pages | 
| game | + | - | game inside twitter (e.g. hangman/quiz) | 
| content | + | - | posts for Twitter audience created content (e.g. poems) | 
| service | + | - | simple service on Twitter (e.g. weather for specific user location) | 
| political | - | + | spams political fake news | 
| fake follower | - | - | manipulates Twitter statistics (e.g. follower/like count) | 
| stock | - | + | spams tweets with stock content, tries to manipulate stock market | 
| social spam | - | + | posts meaningless spam/ads with human behavior | 
| traditional spam | - | -  | posts meaningless spam/ads | 

#### ML Models

The following machine learning models were used for the classification comparison.

- *Baseline*: Logistic Regression (LR)
- Bernoulli Naive Bayes (BNB)
- k-Nearest-Neighbor (KNN)
- Decision Trees (DT)
- Random Forest (RF)
- Neuronal Network (NN)

### TODOs

Some parts of this project need refractoring or improvements:
- refractor methods used by juypter notebooks
- remove unused code parts
- add option to train a machine learning model with precalculated features from command line
- add option to classify an user with a trained machine learning model from command line
- change the language of some graphs in the Jupyter notebooks to English
- add option to calculate only user or tweet features

### Third party notices

The following list contains all used third party file or python modules with the with the corresponding license note:

#### Files:

| File | URL | License | Notice |
| :---: | :---: | :---: | :---: |
| [emoji-test.txt](twitter_bot_type_classification/data/emoji-test.txt) | [link to file](https://unicode.org/Public/emoji/13.0/emoji-test.txt) | [link to license](https://www.unicode.org/license.html) | |
| [html5ents.xml](twitter_bot_type_classification/data/html5ents.xml) | [link to file](https://www.w3.org/2003/entities/2007xml/html5ents.xml) | [link to license](https://www.w3.org/Consortium/Legal/2015/doc-license) | Copyright © 2010 World Wide Web Consortium, (MIT, ERCIM, Keio, Beihang). http://www.w3.org/Consortium/Legal/2015/doc-license |

#### Python modules:

| Module | URL | License |
| :---: | :---: | :---: |
| requests | [project](https://github.com/psf/requests) | [link to license](https://github.com/psf/requests/blob/master/LICENSE) |
| numpy | [project](https://github.com/numpy/numpy) | [link to license](https://github.com/numpy/numpy/blob/master/LICENSE.txt) |
| tweepy | [project](https://github.com/tweepy/tweepy) | [link to license](https://github.com/tweepy/tweepy/blob/master/LICENSE) |
| nltk | [project](https://github.com/nltk/nltk) | [link to license](https://github.com/nltk/nltk/blob/develop/LICENSE.txt) |
| tensorflow | [project](https://github.com/tensorflow/tensorflow) | [link to license](https://github.com/tensorflow/tensorflow/blob/master/LICENSE) |
| scikit-learn | [project](https://github.com/scikit-learn/scikit-learn) | [link to license](https://github.com/scikit-learn/scikit-learn/blob/master/COPYING) |
| botometer | [project](https://github.com/IUNetSci/botometer-python) | [link to license](https://github.com/IUNetSci/botometer-python/blob/master/LICENSE.txt) |
| jupyterlab | [project](https://github.com/jupyterlab/jupyterlab) | [link to license](https://github.com/jupyterlab/jupyterlab/blob/master/LICENSE) |
| plotly | [project](https://github.com/plotly/plotly.py) | [link to license](https://github.com/plotly/plotly.py/blob/master/LICENSE.txt) |
| matplotlib | [project](https://github.com/matplotlib/matplotlib) | [link to license](https://matplotlib.org/users/license.html) |


### License

See [License file](License) for more information.

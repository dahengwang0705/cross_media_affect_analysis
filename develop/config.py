"""
Global configurations
"""

import os

'''
Dirs
'''
# Directory for pickled data
DATA_DIR = './data'

# Directory for temporary data
TMP_DIR = './tmp'

# Directory for figures
FIG_DIR = './fig'

# Directory for news and tweets data by Dr. Meng Jiang
# DEPRECATED
MENG_NEWS_TWEETS_DIR = os.path.join(DATA_DIR, 'raw-news_tweets-meng')

# Directory for original news and tweets data
ORIGINAL_NEWS_TWEETS_DIR = os.path.join(DATA_DIR, 'raw-news_tweets-original')

'''
Files
'''
# DDL scripts to create db, table schema for news, and table schema for tweets
NEWS_TWEETS_DDL_FILE = os.path.join(DATA_DIR, 'original-news_tweets.schema.sql')

# SQLite db for raw news and tweets data (provided by Dr. Meng Jiang)
NEWS_TWEETS_DB_FILE = os.path.join(DATA_DIR, 'original-news_tweets.db')

# Dataframe of news over selected period [2015-01-01, 2015-03-21]
NEWS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'news-period.df.pkl')

# Dataframe of tweets over selected period [2015-01-01, 2015-03-21]
TWEETS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'tweets-period.df.pkl')

'''
Misc
'''
# List of dates when Twitter internal server is unstable and tweets contain errors cannot be parsed
ORIGINAL_TWEETS_ERROR_DATES_LST = ['2015-06-05', '2015-09-20', '2015-09-21', '2015-12-08', '2015-12-09', '2015-12-10', '2016-02-14', '2016-02-15', '2016-02-17', '2016-02-18', '2016-02-19']

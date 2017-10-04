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

'''
Files
'''
# DDL scripts to create db, table schema for news, and table schema for tweets
NEWS_TWEETS_DDL_FILE = os.path.join(DATA_DIR, 'news_tweets-meng.schema.sql')

# SQLite db for raw news and tweets data (provided by Dr. Meng Jiang)
NEWS_TWEETS_DB_FILE = os.path.join(DATA_DIR, 'news_tweets-meng.db')

# Dataframe of news over selected period [2015-01-01, 2015-03-21]
NEWS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'news-period.df.pkl')

# Dataframe of tweets over selected period [2015-01-01, 2015-03-21]
TWEETS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'tweets-period.df.pkl')

'''
Misc
'''

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

# Directory for human-readable data
HR_DIR = './hr'

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

# Dataframe of news over selected period [2014-11-18, 2015-04-14]
NEWS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'news-period.df.pkl')

'''
Misc
'''
# List of dates when Twitter internal server is unstable and tweets contain errors cannot be parsed
ORIGINAL_TWEETS_ERROR_DATES_LST = ['2015-06-05', '2015-09-20', '2015-09-21', '2015-12-08', '2015-12-09', '2015-12-10', '2016-02-14', '2016-02-15', '2016-02-17', '2016-02-18', '2016-02-19']

# Manully selected topics information
MANUALLY_SELECTED_TOPICS_LST = [
    {'category': 'politics', 'name': 'Hillary_Clinton_email_controversy', 'keywords_lst': [('email', 'e-mail'), ('Hillary', 'Clinton')]},
    {'category': 'politics', 'name': 'Iran_nuclear_deal', 'keywords_lst': ['Iran', 'nuclear']},
    {'category': 'politics', 'name': 'Jihadi_John_identity_reveled', 'keywords_lst': ['Jihadi John']},
    {'category': 'social', 'name': 'Ferguson_unrest', 'keywords_lst': ['Ferguson']},
    {'category': 'social', 'name': 'Hong_Kong_protests', 'keywords_lst': ['Hong Kong']},
    {'category': 'social', 'name': 'Sony_cyberattack', 'keywords_lst': ['Sony']},
    {'category': 'social', 'name': 'Bill_Cosby_sexual_assault_allegations ', 'keywords_lst': ['Bill Cosby']},
    {'category': 'social', 'name': 'SpaceX_fails_rocket_landing ', 'keywords_lst': ['SpaceX']},
    {'category': 'social', 'name': 'Brian_Williams_fake_war_story  ', 'keywords_lst': ['Brian Williams']},
    {'category': 'entertainment', 'name': 'Oscar', 'keywords_lst': ['Oscar']},
    {'category': 'entertainment', 'name': 'Super_Bowl', 'keywords_lst': ['Super Bowl']},
    {'category': 'entertainment', 'name': 'Grammy', 'keywords_lst': ['Grammy']},
    {'category': 'entertainment', 'name': 'Golden_Globe', 'keywords_lst': ['Golden Globe']},
    {'category': 'entertainment', 'name': '500_million_Powerball', 'keywords_lst': ['Powerball']},
    {'category': 'disaster', 'name': 'Ebola_virus', 'keywords_lst': ['Ebola']},
    {'category': 'disaster', 'name': 'Indonesia_AirAsia_Flight_QZ8501', 'keywords_lst': [('AirAsia', '8501')]},
    {'category': 'disaster', 'name': 'Paris_attacks', 'keywords_lst': ['Paris']},
    {'category': 'disaster', 'name': 'Vanuatu_Cyclone_Pam', 'keywords_lst': ['Vanuatu', 'Cyclone']},
    {'category': 'disaster', 'name': 'Malaysia_Airlines_Flight_MH370', 'keywords_lst': ['370']},
    {'category': 'holiday', 'name': 'Thanksgiving', 'keywords_lst': ['Thanksgiving']},
    {'category': 'holiday', 'name': 'Black_Friday_and_Cyber_Monday', 'keywords_lst': ['Black Friday', 'Cyber Monday']},
    {'category': 'holiday', 'name': 'Christmas ', 'keywords_lst': ['Christmas ']},
    {'category': 'holiday', 'name': 'New_Year ', 'keywords_lst': ['New Year ']}]

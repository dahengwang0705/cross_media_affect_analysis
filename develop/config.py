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

# Directory for topic_news and topic_tweets docs
TOPICS_DOCS_DIR = os.path.join(HR_DIR, 'topics_docs')

# Directory for EXTERNAL Hedonometer data files
# http://hedonometer.org/index.html
HED_DATA_DIR = os.path.join(DATA_DIR, 'hedonometer')

# Directory of pkls for selected Hedonometer words frequency dicts on topic_tweets docs
TOPICS_TWEETS_SHED_WORDS_FREQ_DICT_PKLS_DIR = os.path.join(DATA_DIR, 'topics_tweets_shed_words_freq_dict_pkls')

# Directory for IBM tweets and news data
IBM_TWEETS_NEWS_DIR = os.path.join(DATA_DIR, 'ibm_tweets_news')


'''
Files
'''
# DDL scripts to create db, table schema for news, and table schema for tweets
NEWS_TWEETS_DDL_FILE = os.path.join(DATA_DIR, 'original-news_tweets.schema.sql')

# SQLite db for raw news and tweets data (provided by Dr. Meng Jiang)
NEWS_TWEETS_DB_FILE = os.path.join(DATA_DIR, 'original-news_tweets.db')

# Pickle of dataframe of news over selected period [2014-11-18, 2015-04-14]
NEWS_PERIOD_DF_PKL = os.path.join(DATA_DIR, 'news-period.df.pkl')

# Pickle of manually selected topics information with associated news and tweets native_id
TOPICS_LST_PKL = os.path.join(DATA_DIR, 'topics.lst.pkl')

# JSON file for Hedonometer happiness words
# Visualization: http://hedonometer.org/words.html
# Download: http://hedonometer.org/api/v1/timeseries/?format=json
HED_WORDS_JSON_FILE = os.path.join(HED_DATA_DIR, 'labMT_words.json')

# Pickle of dataframe for complete Hedonometer happiness words information
HED_WORDS_DF_PKL = os.path.join(DATA_DIR, 'hed_words.df.pkl')

# Pickle of dataframe for Hedonometer selected words
SHED_WORDS_DF_PKL = os.path.join(DATA_DIR, 'shed_words.df.pkl')

# Pickles of dicts for mapping between selected word and word_ind
SHED_WORD_IND_DICT_PKL = os.path.join(DATA_DIR, 'shed_word-ind.dict.pkl')
IND_SHED_WORD_DICT_PKL = os.path.join(DATA_DIR, 'ind-shed_word.dict.pkl')

# Pickle of dict for mapping between and shed_word_ind and shed_word_happs
IND_HAPPS_DICT_PKL = os.path.join(DATA_DIR, 'ind-happs.dict.pkl')

# Pickle of dict for selected Hedonometer words frequency on topic_news docs
TOPICS_NEWS_SHED_WORDS_FREQ_DICT_PKL = os.path.join(DATA_DIR, 'topics_news_shed_words_freq.dict.pkl')


'''
Misc
'''
# List of dates when Twitter internal server is unstable and tweets contain errors cannot be parsed
ORIGINAL_TWEETS_ERROR_DATES_LST = ['2015-06-05', '2015-09-20', '2015-09-21', '2015-12-08', '2015-12-09', '2015-12-10', '2016-02-14', '2016-02-15', '2016-02-17', '2016-02-18', '2016-02-19']

# Manully selected topics information
MANUALLY_SELECTED_TOPICS_LST = [
    {'category': 'politics', 'name': 'Hillary_Clinton_email_controversy', 'keywords_lst': [('email', 'e-mail'), ('Hillary', 'Clinton')]},
    {'category': 'politics', 'name': 'Iran_nuclear_deal', 'keywords_lst': ['Iran', 'nuclear']},
    {'category': 'politics', 'name': 'ISIS_Jihadi_John_identity_reveal', 'keywords_lst': ['Jihadi John']},
    {'category': 'politics', 'name': 'Ukraine_cease_fire', 'keywords_lst': [('cease-fire', 'ceasefire'), ('Ukraine', 'Russia')]},
    {'category': 'politics', 'name': 'Egypt_free_Al_Jazeera_journalist', 'keywords_lst': [('Al Jazeera', 'Egypt'), ('Peter Greste', 'journalist')]},
    {'category': 'politics', 'name': 'Keystone_XL_Pipeline_bill', 'keywords_lst': ['Keystone XL']},
    {'category': 'politics', 'name': 'CIA_Torture_Report', 'keywords_lst': ['Torture Report']},
    {'category': 'politics', 'name': 'Obama_cybersecurity_plan', 'keywords_lst': ['Obama', 'cyber']},
    {'category': 'politics', 'name': 'DHS_funding_issue', 'keywords_lst': ['DHS', 'fund']},
    {'category': 'politics', 'name': 'US_Cuba_relationship', 'keywords_lst': [('US', 'Obama'), ('Cuba', 'Castro')]},
    {'category': 'politics', 'name': '2015_CPAC', 'keywords_lst': ['CPAC']},
    {'category': 'politics', 'name': 'Iraq_free_ISIS_Tikrit', 'keywords_lst': ['Tikrit']},
    {'category': 'politics', 'name': 'Nigeria_Boko_Haram_terrorists', 'keywords_lst': ['Boko Haram']},
    
    {'category': 'social', 'name': 'Ferguson_unrest', 'keywords_lst': ['Ferguson']},
    {'category': 'social', 'name': 'Hong_Kong_protest', 'keywords_lst': ['Hong Kong']},
    {'category': 'social', 'name': 'Sony_cyberattack', 'keywords_lst': ['Sony']},
    {'category': 'social', 'name': 'Bill_Cosby_sexual_assault_allegation', 'keywords_lst': ['Bill Cosby']},
    {'category': 'social', 'name': 'SpaceX_rocket_landing', 'keywords_lst': ['SpaceX']},
    {'category': 'social', 'name': 'Brian_Williams_fake_story', 'keywords_lst': ['Brian Williams']},
    {'category': 'social', 'name': 'HSBC_tax_scandal', 'keywords_lst': ['HSBC']},
    {'category': 'social', 'name': 'David_Carr_death', 'keywords_lst': ['David Carr']},
    {'category': 'social', 'name': 'Patriots_Deflategate', 'keywords_lst': [('Deflategate', 'Deflate-gate')]},
    {'category': 'social', 'name': 'Delhi_Uber_driver_rape', 'keywords_lst': ['Uber', ('rape', 'Delhi')]},
    {'category': 'social', 'name': 'Superbug_spread', 'keywords_lst': ['Superbug']},
    {'category': 'social', 'name': 'Rudy_Giuliani_Obama_critique', 'keywords_lst': ['Giuliani']},
    #{'category': 'social', 'name': 'Ben_Carson_homosexuality_issue', 'keywords_lst': ['Ben Carson', ('gay', 'homosexuality')]},
    
    {'category': 'entertainment', 'name': 'Oscar', 'keywords_lst': ['Oscar']},
    {'category': 'entertainment', 'name': 'Super_Bowl', 'keywords_lst': ['Super Bowl']},
    {'category': 'entertainment', 'name': 'Grammy', 'keywords_lst': ['Grammy']},
    {'category': 'entertainment', 'name': 'Golden_Globe', 'keywords_lst': ['Golden Globe']},
    {'category': 'entertainment', 'name': '500_million_Powerball', 'keywords_lst': ['Powerball']},
    {'category': 'entertainment', 'name': 'Thanksgiving', 'keywords_lst': ['Thanksgiving']},
    {'category': 'entertainment', 'name': 'Black_Friday_and_Cyber_Monday', 'keywords_lst': [('Black Friday', 'Cyber Monday')]},
    {'category': 'entertainment', 'name': 'Christmas', 'keywords_lst': ['Christmas']},
    {'category': 'entertainment', 'name': 'New_Year', 'keywords_lst': ['New Year']},
    {'category': 'entertainment', 'name': 'Apple_Watch', 'keywords_lst': ['Apple Watch']},
    {'category': 'entertainment', 'name': 'Yosemite_historic_climb', 'keywords_lst': [('Yosemite', 'El Capitan')]},
    {'category': 'entertainment', 'name': 'Jon_Stewart_Daily_Show', 'keywords_lst': ['Jon Stewart']},
    {'category': 'entertainment', 'name': 'success_of_American_Sniper', 'keywords_lst': ['American Sniper']},

    {'category': 'tragedy', 'name': 'Ebola_virus_spread', 'keywords_lst': ['Ebola']},
    {'category': 'tragedy', 'name': 'Indonesia_AirAsia_Flight_QZ8501_crash', 'keywords_lst': [('AirAsia', '8501')]},
    {'category': 'tragedy', 'name': 'Paris_attacks', 'keywords_lst': ['Paris']},
    {'category': 'tragedy', 'name': 'Vanuatu_Cyclone_Pam', 'keywords_lst': ['Vanuatu', 'Cyclone']},
    {'category': 'tragedy', 'name': 'Malaysia_Airlines_Flight_MH370_crash', 'keywords_lst': ['370']},
    {'category': 'tragedy', 'name': 'Colorado_NAACP_bombing', 'keywords_lst': ['NAACP']},
    {'category': 'tragedy', 'name': 'FSU_shooting', 'keywords_lst': ['FSU']},
    {'category': 'tragedy', 'name': 'Chapel_Hill_shooting', 'keywords_lst': ['Chapel Hill']},
    {'category': 'tragedy', 'name': 'Bobbi_Kristina_Brown_death', 'keywords_lst': ['Bobbi Kristina Brown']},
    {'category': 'tragedy', 'name': 'Taliban_Pakistan_school_massacre', 'keywords_lst': [('Pakistan', 'Taliban'), ('school', 'student', 'massacre')]},
    {'category': 'tragedy', 'name': 'American_ISIS_Hostage_Kayla_Mueller', 'keywords_lst': ['Kayla Mueller']},
    {'category': 'tragedy', 'name': 'TransAsia_Airways_Flight_GE235_crash', 'keywords_lst': [('TransAsia', 'Taiwan'), ('plane', 'crash', 'pilot', 'flight')]},
    {'category': 'tragedy', 'name': 'Germanwings_Flight_9525_crash', 'keywords_lst': [('Germanwings', 'Lufthansa', '9525')]}]

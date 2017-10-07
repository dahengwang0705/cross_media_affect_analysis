"""
Utility functions
"""

import time

'''
Template of news post_time string

Example: 'Mon, 17 Nov 2014 21:04:21 -0800'
'''
NEWS_POST_TIME_TEMPLATE = '%a, %d %b %Y %H:%M:%S %z'

'''
Template of tweet post_time string

Example: 'Tue Nov 18 06:48:16 +0000 2014'
'''
TWEET_POST_TIME_TEMPLATE = "%a %b %d %H:%M:%S %z %Y"

STANDARD_DATETIME_TEMPLATE = "%Y-%m-%d %H:%M:%S"
SIMPLE_DATE_TEMPLATE = "%Y-%m-%d"

def parse_news_post_time(news_post_time_str):
    news_timestamp = time.strptime(news_post_time_str, NEWS_POST_TIME_TEMPLATE)
    return time.strftime(STANDARD_DATETIME_TEMPLATE, news_timestamp)

def parse_tweet_post_time(tweet_post_time_str):
    tweet_timestamp = time.strptime(tweet_post_time_str, TWEET_POST_TIME_TEMPLATE)
    return time.strftime(STANDARD_DATETIME_TEMPLATE, tweet_timestamp)

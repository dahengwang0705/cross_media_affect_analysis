"""
Utility functions
"""

import time
import collections

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
    """
    Pasrse String in NEWS_POST_TIME_TEMPLATE format into String in STANDARD_DATETIME_TEMPLATE format
    
    PARAM news_post_time_str: String in NEWS_POST_TIME_TEMPLATE format
    RETURN: parsed String in STANDARD_DATETIME_TEMPLATE format
    """
    news_timestamp = time.strptime(news_post_time_str, NEWS_POST_TIME_TEMPLATE)
    return time.strftime(STANDARD_DATETIME_TEMPLATE, news_timestamp)

def parse_tweet_post_time(tweet_post_time_str):
    """
    Pasrse String in TWEET_POST_TIME_TEMPLATE format into String in STANDARD_DATETIME_TEMPLATE format
    
    PARAM tweet_post_time_str: String in TWEET_POST_TIME_TEMPLATE format
    RETURN: parsed String in STANDARD_DATETIME_TEMPLATE format
    """
    tweet_timestamp = time.strptime(tweet_post_time_str, TWEET_POST_TIME_TEMPLATE)
    return time.strftime(STANDARD_DATETIME_TEMPLATE, tweet_timestamp)

def news_title_match(news_title, topic_keywords_lst, verbose=False, case_sensitive=False):
    """
    Check if a news title contians keywords of a topic. All keywords in list should appear in the news title for it
    to be qualified as a match. If a keyword is a tuple of items, any item appears in news title mark this news title
    contains this tuple keyword.
    
    PARAM news_title: String of news title
    PARAM topic_keywords_lst: list of keywords of the topic. Keyword can be a single String or tuple of items.
    
    RETURN: True or False if the news title contains topic keywords
    """
    keywords_match = True
    if verbose: print('NEWS TITLE: {}'.format(news_title))
    for keyword_ind, keyword in enumerate(topic_keywords_lst):
        if isinstance(keyword, tuple):
            if verbose: print('({}/{}) Tuple keyword: {}'.format(keyword_ind+1, len(topic_keywords_lst), keyword))
            keyword_match = False
            for item in keyword:
                if verbose: print('\tTuple item: ({})'.format(item), end='; ')
                
                if case_sensitive:
                    contains_item = item in news_title
                else:
                    contains_item = item.lower() in news_title.lower()
                
                if verbose: print('Contains?: {}'.format(contains_item))
                keyword_match = keyword_match or contains_item
            if verbose: print('\tContains Tuple?: {}'.format(keyword_match))
            keywords_match = keywords_match and keyword_match
        else:
            if verbose: print('({}/{}) Keyword: {}'.format(keyword_ind+1, len(topic_keywords_lst), keyword))
                
            if case_sensitive:
                keyword_match = keyword in news_title
            else:
                keyword_match = keyword.lower() in news_title.lower()
            
            if verbose: print('\tContains?: {}'.format(keyword_match))
            keywords_match = keywords_match and keyword_match
    if verbose: print('MATCH?: {}'.format(keywords_match), end='\n\n')
    return keywords_match


# 20171019-daheng-build_shed_words_freq_dicts
def count_tweet_shed_words_freq(tweet_text, ind_shed_word_dict, shed_word_ind_dict, shed_words_set):
    """
    Count the frequency of selected Hedonometer words in tweet text.
    
    param tweet_text: String of text field of tweet
    
    return: dict of shed_word_ind to shed_word_freq mapping
    """
    
    '''
    Tokenize and count words in tweet text
    
    Ref
     - 'We defined a word as any contiguous set of characters bounded by white space and/or a small set of punctuation characters.'
     - 'We therefore included all misspellings, words from any language used on Twitter, hyperlinks, etc.'
     - 'All pattern matches we made were case-insensitive, and we did not perform stemming.'
    '''
    tweet_text_words = tweet_text.lower().split()
    counter = collections.Counter(tweet_text_words)
    
    tweet_shed_words_freq_dict = {int(shed_word_ind_dict[tweet_text_word]): int(tweet_text_word_freq)
                                  for tweet_text_word, tweet_text_word_freq in list(counter.items()) if tweet_text_word in shed_words_set}
    
    return tweet_shed_words_freq_dict


# 20171019-daheng-build_shed_words_freq_dicts
def count_news_doc_shed_words_freq(news_doc, ind_shed_word_dict, shed_word_ind_dict, shed_words_set):
    """
    Similar to the 'count_tweet_shed_words_freq' function.
    Count the frequency of selected Hedonometer words in news_doc field.
    
    param news_doc: String of news_doc field of a news article
    
    return: dict of shed_word_ind to shed_word_freq mapping
    """
    
    # replace special new paragraph mark '::::::::' in news_doc field with white space
    news_doc = news_doc.replace('::::::::', ' ')
    
    news_doc_words = news_doc.lower().split()
    counter = collections.Counter(news_doc_words)
    
    news_doc_shed_words_freq_dict = {int(shed_word_ind_dict[news_doc_word]): int(news_doc_word_freq)
                                     for news_doc_word, news_doc_word_freq in list(counter.items())
                                     if news_doc_word in shed_words_set}
    
    return news_doc_shed_words_freq_dict


def merge_shed_words_freq_dicts(shed_words_freq_dicts_lst, verbose=False):
    """
    Merge a lst of shed_words_freq_dicts into a single shed_words_freq_dict
    
    param shed_words_freq_dicts_lst: a lst of shed_words_freq_dicts
    
    return: a single merged shed_words_freq_dict
    """
    merged_freq_counter = collections.Counter()
    if verbose:
        print('(FUNC) NUM OF DICTS: {}'.format(len(shed_words_freq_dicts_lst)))
    
    for shed_words_freq_dict in shed_words_freq_dicts_lst:
        merged_freq_counter.update(collections.Counter(shed_words_freq_dict))
    
    return dict(merged_freq_counter)


def compute_h_score(shed_words_freq_dict, shed_words_happs_dict, verbose=False):
    """
    Compute the happiness score given a shed_words_freq_dict and a shed_words_freq_dict
    
    param shed_words_freq_dict: dict of shed_word_ind to shed_word_freq mapping
    param shed_words_happs_dict: dict of shed_word_ind to shed_word_happs mapping
    
    return: a single happiness score
    """
    total_len = sum(shed_words_freq_dict.values())
    if verbose:
        print('(FUNC) LEN: {}'.format(total_len))
    
    # intermediate dict for each shed word contribution to the last total happiness score
    shed_words_contri_dict = {shed_word_ind: (shed_words_happs_dict[shed_word_ind] * (shed_words_freq / total_len)) 
                              for shed_word_ind, shed_words_freq in list(shed_words_freq_dict.items())}
    if verbose:
        print('(FUNC) SHED WORDS CONTRIBUTIONS: {}'.format(shed_words_contri_dict))
    
    h_score = sum(shed_words_contri_dict.values())
    
    return h_score


if '__main__' == __name__:
    """
    Tests on news_title_match() function
    """
    print('TESTS on news_title_match() function...')
    test_topic_dict = {'cat': 'politics',
                       'name': 'Hillary_Clinton_email_controversy',
                       'keywords_lst': [('email', 'e-mail'), ('hillary', 'Clinton')]}
    
    test_news_titles = ["Hillary Clinton's Personal Email Use May Have Violated Federal Requirements ...", 
                        "Clinton had no official State Dept. email address",
                        "No entitlement reform: Hillary email scandal reveals core weakness",
                        "House panel issues subpoenas for Clinton e-mails",
                        "Ferguson cop e-mails insult Obamas"]
    
    for news_title in test_news_titles:
        news_title_match(news_title, test_topic_dict['keywords_lst'], verbose=True)

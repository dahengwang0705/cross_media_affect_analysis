"""
Worker functions for multiprocessing
"""

import json
import multiprocessing
import sys
import time
import pymongo
import os

import mongodb
import utilities


def find_keywords_in_tweet_text(db_name, collection_name, process_ind, process_num, process_file, kws_lst):
    """
    Tag whether a list of keywords appears in tweet_text field
    
    :param db_name: the name of the MongoDB database
    :param collection_name: the name of the collection
    :param process_ind: the index of this process (min: 0; max: processes number minus 1)
    :param process_num: the total nubmer of processes working together
    :param process_file: the output file of this process
    :param kws_lst: a list of target keywords
    """
    
    '''
    Establish connection to MongoDB database and query batch of tweets
    '''
    col = mongodb.initialize(db_name=db_name, collection_name=collection_name)
    
    col_size = col.count()
    batch_size = col_size // process_num
    skip = process_ind * batch_size
    limit = batch_size
    if process_ind == (process_num - 1): # if this is the last batch, process all left
        limit = col_size - skip + 1
    
    time.sleep(process_ind) # asynchronize start time to reduce the peak burden of MongoDB database
    
    print('Process-{}/{} handling documents {} to {}...'.format(process_ind, process_num, skip, skip + limit - 1))
    cursor = col.find(sort=[('_id', pymongo.ASCENDING)], # sort by default '_id' ascending
                      projection={'_id': 0},
                      skip=skip,
                      limit=limit)
    
    '''
    Tag the 'text' field for each keyword in the list
    '''   
    with open(process_file, 'w') as f:
        for doc in cursor:
            tweet_text = doc['text']
            
            for kw_ind, kw in enumerate(kws_lst):
                if kw.lower() in tweet_text.lower():
                    f.write(json.dumps(doc) + '\n')
                    break

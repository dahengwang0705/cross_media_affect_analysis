"""
Get connection to (local) MongoDB database
"""

import pymongo
from pymongo import MongoClient
from pymongo import errors


def initialize(db_name: object, collection_name: object, host: object = 'localhost', port: object = 27017) -> object:
    """
    Initialize connection to MongoDB database and get collection object
    
    :param db_name:
    :param collection_name:
    :param host:
    :param port:
    :return: collection obj
    """
    try:
        client = MongoClient(host, port)
        db = client[db_name]
        collection = db[collection_name]
        print('MongoDB on {}:{}/{}.{} connected successfully!'.format(host, port, db_name, collection_name))
        return collection
    except pymongo.errors.ConnectionFailure as e:
        print('MongoDB on {}:{} connection failed: {}'.format(host, port, e))

        
def initialize_db(db_name: object, host: object = 'localhost', port: object = 27017) -> object:
    """
    Initialize connection to MongoDB database and get database object
    
    :param db_name:
    :param collection_name:
    :param host:
    :param port:
    :return: db obj
    """
    try:
        client = MongoClient(host, port)
        db = client[db_name]
        print('MongoDB on {}:{}/{} connected successfully!'.format(host, port, db_name))
        return db
    except pymongo.errors.ConnectionFailure as e:
        print('MongoDB on {}:{} connection failed: {}'.format(host, port, e))


def test_connection():
    print('Test MongoDB connection successful!')

if __name__ == '__main__':
    test_connection()

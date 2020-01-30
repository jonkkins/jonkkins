from pymongo import MongoClient
from config import config
import urllib.parse


def mongo():
    username = urllib.parse.quote_plus(config()['db']['username'])
    password = urllib.parse.quote_plus(config()['db']['password'])
    host = config()['db']['host']
    return MongoClient('mongodb://%s:%s@%s' % (username, password, host))

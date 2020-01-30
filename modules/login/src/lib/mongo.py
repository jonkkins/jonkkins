from pymongo import MongoClient
from lib.config import config
import urllib.parse


class Mongo:

    __conn__ = None
    __DB_NAME__ = 'login'

    @staticmethod
    def conn():
        username = urllib.parse.quote_plus(config()['db']['username'])
        password = urllib.parse.quote_plus(config()['db']['password'])
        host = config()['db']['host']

        if Mongo.__conn__ is None:
            Mongo.__conn__ = MongoClient('mongodb://%s:%s@%s' % (username, password, host))

        return Mongo.__conn__

    @staticmethod
    def db():
        return Mongo.conn()[config()['db']['db_prefix'] + Mongo.__DB_NAME__]


def mongo():
    return Mongo.conn()


def db():
    return Mongo.db()

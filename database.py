import pymongo


class Database:
    uri = "mongodb://127.0.0.1:27017"
    DATABASE=None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, post):
        return Database.DATABASE[collection].insert(post)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
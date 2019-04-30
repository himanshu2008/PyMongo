import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.mydatabase
Users = db.users
a = Users.count()
print(a)
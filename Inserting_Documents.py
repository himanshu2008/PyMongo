import pymongo
from pymongo import MongoClient

# To instantiate Mongo Client
myClient = MongoClient()
# To access database
db = myClient.mydatabase
# To create collection(tables)
users = db.users
user1 = {"Username": "Himanshu", "Password": "password", "Favourite_Number": 445, "Hobbies": ["Python", "Games", "Pizza"]}
user_id = users.insert_one(user1).inserted_id
print(user_id)
# To insert multiple users at one
mylist = [
    {"Username": "Second", "Password": "1234"},
    {"Username": "Red", "Password": "blue"}]
x = users.insert_many(mylist)
print(x.inserted_ids)
a = users.count()
print(a)
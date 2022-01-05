CONNECTION = "mongodb+srv://marklawrence:mongodb01@cluster0.ukgck.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

from pymongo import MongoClient
import pymongo

mongo_client = MongoClient(CONNECTION)

dbname = mongo_client["todo_list"]

items_col = dbname["todo_items"]

for x in items_col.find({},{'_id': '61a0c0dbb11c08301cb3a307','Item_name':1}):
    print(x)



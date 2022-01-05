from pymongo import MongoClient
import pymongo


CONNECTION = 'mongodb+srv://marklawrence:mongodb01@cluster0.ukgck.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

item_dataset = [ {
    "Item_number": "ItemNo_1",
    "Item_name": "Play football",
    "Item_description": "Go for a kick about over the field",
    "Status": "Not started"
},

{
    "Item_number": "ItemNo_2",
    "Item_name": "Walk the dogs",
    "Item_description": "Throw the dogs into the back of the car and drive to the park",
    "Status": "Not started"
    }
]

def init_db():

    mongo_client = MongoClient(CONNECTION, connect=False)

    dbname = mongo_client["todo_list"]

    items_col = dbname["todo_items"]

    items_col.insert_many(item_dataset)


init_db()
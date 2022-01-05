from flask.wrappers import Request
from pymongo import MongoClient
import pymongo
from flask import Flask, render_template, redirect, url_for, request

CONNECTION = 'mongodb+srv://marklawrence:mongodb01@cluster0.ukgck.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
MONGODB = "todo_list"
MONGOCOLLECTION = "todo_items"

app = Flask(__name__)


def mongodb_connection():
    mongo_client = MongoClient(CONNECTION)
    dbname = mongo_client[MONGODB]
    return dbname

def mongodb_getcollections():
    dbname = mongodb_connection()
    item_col = dbname[MONGOCOLLECTION]
    x = []
    for i in item_col.find():
        x.append(i)
    return x


print(mongodb_getcollections())        #return render_template ('index.html')
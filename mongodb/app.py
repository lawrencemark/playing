from flask.wrappers import Request
from pymongo import MongoClient
import pymongo
from flask import Flask, render_template, redirect, url_for, request
import time
import random

CONNECTION = 'mongodb+srv://marklawrence:mongodb01@cluster0.ukgck.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
MONGODB = "todo_list"
MONGOCOLLECTION = "todo_items"

itemList = []

app = Flask(__name__)

def mongodb_connection():
    mongo_client = MongoClient(CONNECTION)
    dbname = mongo_client[MONGODB]
    return dbname

def mongodb_getcollections():
    itemList.clear()
    dbname = mongodb_connection()
    item_col = dbname[MONGOCOLLECTION]
    for i in item_col.find():
        itemList.append(i)

def mongodb_addcollection(taskName,taskDesc,taskStatus):
    item_Number = f'ItemNo_{random.randrange(1,1000000)}'
    item_Name = taskName
    item_Description = taskDesc
    Status = taskStatus
    
    if (len(item_Number) > 0) and (len(item_Name) > 0) and (len(taskStatus) > 0):
         
        item_collection = {
            "Item_number": item_Number,
            "Item_name": item_Name,
            "Item_description": item_Description,
            "Status": Status
        } 
         
        dbname = mongodb_connection()
        item_col = dbname[MONGOCOLLECTION]
        item_col.insert_one(item_collection)

def mongodb_delcollection(item_Number):
    query = { "Item_number": item_Number}
    dbname = mongodb_connection()
    item_col = dbname[MONGOCOLLECTION]
    item_col.delete_one(query)

def mongodb_updatecollection(item_Number, status):
    query = { "Item_number": item_Number}
    replaceStatus = { "$set": {"Status": status } }
    dbname = mongodb_connection()
    item_col = dbname[MONGOCOLLECTION]
    item_col.update_one(query, replaceStatus)

@app.route("/",methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        taskName = request.form['tname']
        taskDesc = request.form['tdesc']
        taskStatus = request.form['tstatus']
        
        mongodb_addcollection(taskName,taskDesc,taskStatus)
        return redirect(url_for('index'))

    else:
        mongodb_getcollections()
        return render_template ('index.html', results=itemList)


@app.route("/update/<itemNumber>",methods = ['POST', 'GET'])
def update(itemNumber):
    status = request.form['status']
    if request.method == 'POST':
        if status == 'delete':
            mongodb_delcollection(itemNumber)
            return redirect(url_for('index'))
        else:
            mongodb_updatecollection(itemNumber,status)
            return redirect(url_for('index'))

     

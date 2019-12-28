import pymongo
import datetime

DB_ADDRESS = "mongodb://localhost:27017/"
DB_NAME = "myItemsList"
ITEM_LIST = "myFollowedItems"
PRICE_HISTORY = "myPriceHistory" 

myclient = pymongo.MongoClient(DB_ADDRESS)
db = myclient[DB_NAME]

itemList = db[ITEM_LIST]
priceList = db[PRICE_HISTORY]

def insertItem(url):
    itemList.insert_one({"url": url})

def getItems():
    items = itemList.find({})
    return items

def deleteItem(url): 
    itemList.delete_one({"url": url})

def printItems():
    items = getItems()
    for i in items:
        print(i)

def addPrice(itemId, price):
    priceList.insert_one({"itemId": itemId, "price": price, "date": datetime.datetime.utcnow() })

def getPrices():
    prices = priceList.find({})
    return prices 

def printPrices():
    prices = getPrices() 
    for i in prices:
        print(i)

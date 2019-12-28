import requests
from bs4 import BeautifulSoup 
from threading import Timer 
import database 
import time 

def getPrice(url, session = requests.session()):
    getPriceRequest = session.get(url)
    soup = BeautifulSoup(getPriceRequest.content, features="html.parser")
    # in a div class, find the element that has the price
    return soup.find("div", {"ng-bind-html":"productData.product.sellPrice"}).getText()

def getDailyPrice():
    items = database.getItems()
    for i in items:
        price = getPrice(i["url"])
        database.addPrice(i["_id"], price)

def triggerDaily():
    timer = Timer(1.0, getDailyPriceRecursive)
    timer.start()

def getDailyPriceRecursive():
    getDailyPrice()
    time.sleep(10)
    getDailyPriceRecursive()
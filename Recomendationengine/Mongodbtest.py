#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html

import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.profiles

products = col.find()


for x in products:
    print(x)

print(db)



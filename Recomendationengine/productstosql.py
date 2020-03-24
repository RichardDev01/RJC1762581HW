#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.huwebshop

col = db.products

products = col.find()

conn = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_p;")

cur.execute("CREATE TABLE all_p (_ID varchar PRIMARY KEY, "
            "data varchar, "
            "price integer, "
            "sub_category varchar, "
            "sub_sub_category varchar, "
            "gender varchar, "
            "color varchar, "
            "herhaalaankoop varchar,"
            "brand varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in products:
    cur.execute("INSERT INTO all_p (_ID, data, price, sub_category, sub_sub_category, gender, color, herhaalaankoop, brand) VALUES (%s, %s, %s,%s, %s, %s,%s, %s,%s)",
                (i['_id'],
                 i['name'] if 'name' in i else None,
                 i['price']['selling_price'] if 'price' in i else None,
                 i['sub_category'] if 'sub_category' in i else None,
                 i['sub_sub_category'] if 'sub_sub_category' in i else None,
                 i['gender'] if 'gender' in i else None,
                 i['color'] if 'color' in i else None,
                 i['herhaalaankoop'] if 'herhaalaankoop' in i else None,
                 i['brand'] if 'brand' in i else None))
#ID, category, brand, gender, sub category, sub sub category, color, name, price
"""
# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")
"""
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
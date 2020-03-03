#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.products

products = col.find()
#print(products[0])
#print(products[0]['name'])
#for x in products:
#    print(x)

print(db)

conn = psycopg2.connect("dbname=voordeelshop user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS test;")

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, _ID integer, data varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in range (0,5):
    cur.execute("INSERT INTO test (_ID, data) VALUES (%s, %s)",(products[i]['_id'], products[i]['name']))
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
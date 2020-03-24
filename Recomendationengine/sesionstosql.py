#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.sessions

sessions = col.find()

print(db)

conn = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_se;")

cur.execute("CREATE TABLE all_se (_ID varchar PRIMARY KEY, "
            "buid varchar, has_sale varchar, segment varchar, preferences varchar, itorder varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
count =0
for i in sessions[:10000]:
    cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                (str(i['_id']),
                 str(i['buid']) if 'buid' in i else None,
                 str(i['has_sale']) if 'has_sale' in i else None,
                 str(i['preferences']) if 'preferences' in i else None,
                 str(i['order']) if 'order' in i else None,
                 str(i['segment']) if 'segment' in i else None))
    count +=1
    if count % 1000 == 0:
        print(count)
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



'''
#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.sessions

sessions = col.find()

print(db)

conn = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_se;")

cur.execute("CREATE TABLE all_se (_ID varchar PRIMARY KEY, "
            "buid varchar, has_sale varchar, preferences varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)

print(sessions[0])
count = 0
for i in sessions[:65000]:
    try:
        cur.execute("INSERT INTO all_se (_ID, buid, has_sale,preferences) VALUES (%s, %s,%s,%s)",
                    (str(i['_id']),
                     i['buid'] if 'buid' in i else None,
                     i['has_sale'] if 'has_sale' in i else None,
                     list(i['preferences']) if 'preferences' in i else None,))
    except:
        print("nope")
        continue
    count +=1
    if count % 1000 == 0:
        print(count)

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
'''
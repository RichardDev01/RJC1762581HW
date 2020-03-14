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

conn = psycopg2.connect("dbname=voordeelshop user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_se;")

cur.execute("CREATE TABLE all_se (id serial PRIMARY KEY, "
            "_ID varchar, session_start varchar, session_end varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in sessions:
    cur.execute("INSERT INTO all_se (_ID, session_start, session_end) VALUES (%s, %s, %s)",
                (str(i['_id']),
                 i['session_start'] if 'session_start' in i else None,
                 i['session_end'] if 'session_end' in i else None))
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
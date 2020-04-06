#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.sessions

sessions = col.find()

print(db)

conn = psycopg2.connect("dbname=voordeelschoptest user=postgres password=kip")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_se;")

cur.execute("CREATE TABLE all_se (_ID varchar PRIMARY KEY, "
            "buid varchar, has_sale varchar, segment varchar, preferences varchar, itorder varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
count = 0
for i in sessions:

    try:
        preferenceval = {}

        try:
            preference = i['preferences']['brand']
            newlist = list()
            for j in preference.keys():
                newlist.append(j)
                break

            preferenceval = newlist[0]

            preferenceval = str(preferenceval)
            cur.execute("select idbrand from brand where brandnaam = '{}' ".format(preferenceval))
            info = cur.fetchall()

            brandnaam = info[0][0]
            cur.execute("SELECT id FROM product where brand_idbrand = {} ORDER BY RANDOM() LIMIT 1;".format(brandnaam))
            proid = cur.fetchall()
            #print(proid[0][0])
            preferenceval = "{" + proid[0][0]+ "}"

            '''
            preference = i['preferences']['brand']
            {k: v for k, v in sorted(preference.items(), key=lambda item: item[1])}
            print(preference.keys())
            preferenceval = newlist
            print(preferenceval)
            '''
        except:
            preferenceval = "{}"

        orderstring = "{"
        try:
            for j in range (len(i['order']['products'])):
                #print(i['order']['products'][j].get('id'),end= " ")
                orderstring += i['order']['products'][j].get('id') + ","
            orderstring = orderstring[:-1]
            orderstring += "}"
        except:
            orderstring = "{}"



        cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                    (str(i['_id']),
                     str(i['buid']) if 'buid' in i else None,
                     str(i['has_sale']) if 'has_sale' in i else None,
                     preferenceval,
                     #str(i['preferences']['brand']) if 'preferences' in i else None,
                     #str(i['order']['products'][0]) if 'products' in i else None,
                     orderstring,
                     str(i['segment']) if 'segment' in i else None))

        '''
        cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES ('{}', '{}','{}','{}','{}','{}')".format(str(i["_id"]), i["buid"] if "buid" in i else None, str(i["has_sale"]) if "has_sale" in i else None, preferenceval,orderstring, str(i["segment"]) if "segment" in i else None))
        '''

    except:

        try:
            orderstring = "{"
            try:
                for j in range (len(i['order']['products'])):
                    #print(i['order']['products'][j].get('id'),end= " ")
                    orderstring += i['order']['products'][j].get('id') + ","
                orderstring = orderstring[:-1]
                orderstring += "}"
            except:
                orderstring = "{}"

            cur.execute("INSERT INTO all_se (_ID, buid, has_sale, preferences,itorder,segment) VALUES (%s, %s,%s,%s,%s,%s)",
                        (str(i['_id']),
                         str(i['buid']) if 'buid' in i else None,
                         str(i['has_sale']) if 'has_sale' in i else None,
                         str("{}"),
                         #str(i['preferences']['brand']) if 'preferences' in i else None,
                         #str(i['order']['products'][0]) if 'products' in i else None,
                         orderstring,
                         str(i['segment']) if 'segment' in i else None))
        except:
            if count % 1000 == 0:
                print(count, "Sessions")
                print("error")
                conn.commit()

        if count % 1000 == 0:
            print(count, "Sessions")
            print("error")
            conn.commit()


    count += 1


    if count % 1000 == 0:
        print(count, "Sessions")
        conn.commit()

print("done with sessions")
conn.commit()
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
"""
select profiles.id, profiles.latestactivity, sessions.duration, profiles_previously_viewed.prodid, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from profiles
right JOIN sessions ON profiles.id=sessions.profid
right JOIN profiles_previously_viewed ON profiles.id=profiles_previously_viewed.profid
right JOIN products ON products.id=profiles_previously_viewed.prodid

select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products WHERE products.deal IS NOT NULL and products.category is not null
order by category, subcategory, targetaudience,deal asc

"""

#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2

conn = psycopg2.connect("dbname=voordeelopdracht user=postgres password=kip")
cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS test;")

#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, _ID integer, data varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)


# Query the database and obtain data as Python objects
#cur.execute("SELECT * FROM products;")
#cur.execute("select profiles.id, profiles.latestactivity, sessions.duration, profiles_previously_viewed.prodid, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from profiles right JOIN sessions ON profiles.id=sessions.profid right JOIN profiles_previously_viewed ON profiles.id=profiles_previously_viewed.profid right JOIN products ON products.id=profiles_previously_viewed.prodid")
#cur.execute("select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products order by id asc")
cur.execute("select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products WHERE products.deal IS NOT NULL and products.category is not null order by category, subcategory, targetaudience,deal asc")
rows = cur.fetchall()

categorydict = {}
subcategorydict = {}
genderdict = {}

for row in rows:
    if  isinstance(row[[1][0]], str)== True:
        if row[1] in categorydict:
            categorydict[row[1]] += 1
        else:
            categorydict[row[1]] = 1
    if row[1] in categorydict:
        categorydict[row[1]] += 1
    else:
        categorydict[row[1]] = 1

    if  isinstance(row[[2][0]], str)== True:
        if row[2] in subcategorydict:
            subcategorydict[row[2]] += 1
        else:
            subcategorydict[row[2]] = 1
    if row[2] in subcategorydict:
        subcategorydict[row[2]] += 1
    else:
        subcategorydict[row[2]] = 1


    if isinstance(row[[3][0]], str) == True:
        if row[3] in genderdict:
            genderdict[row[3]] += 1
        else:
            genderdict[row[3]] = 1
    if row[3] in genderdict:
        genderdict[row[3]] += 1
    else:
        genderdict[row[3]] = 1

    #print(row[1])
categorylst= []
subcategorylst= []
genderlst =[]
for keys in categorydict.keys():
    categorylst.append(keys)
for keys in subcategorydict.keys():
    subcategorylst.append(keys)
for keys in genderdict.keys():
    genderlst.append(keys)


#for i in range(0,len(categorylst)):
    # De i heeft de category waarmee we gaan sorteren
for j in range(0, len(subcategorylst)):
    #De j heeft de subcategory waarmee we gaan sorten

    for k in range(0, len(genderlst)):
        count = 0
        for row in rows:
            #De i heeft de category waarmee we gaan sorteren
            if count == 2:
                break
            if (subcategorylst[j] in row and genderlst[k] in row):
                print(row)
                count += 1

for i in range(0,len(categorylst)):
    # De i heeft de category waarmee we gaan sorteren
    for k in range(0, len(genderlst)):
        count = 0
        for row in rows:
            #De i heeft de category waarmee we gaan sorteren
            if count == 2:
                break
            if (subcategorylst[i] in row and genderlst[k] in row):
                print(row)
                count += 1

'''
woorden = []
woordenteller = {}
namen()

for woord in woorden:
    if woord in woordenteller:
        woordenteller[woord] += 1
    else:
        woordenteller[woord] = 1
'''



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
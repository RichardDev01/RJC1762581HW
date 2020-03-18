#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2

def recomendeditems(category,subcategory,targetaudience):
    #Hier maak ik gebruik van een SQL statement die in mijn Recomended items table alleen maar de producten hallen die overeen komen de gegeven category, subcategory en target audience(kunnen maximaal 5 items zijn*)
    cur.execute("select recomendedpro._id, recomendedpro.category, recomendedpro.sub_category, recomendedpro.targetaudience from recomendedpro  where category = '{}'and sub_category = '{}' and targetaudience = '{}'".format(category,subcategory,targetaudience))
    info = cur.fetchall()
    return info

def createrecomendeditemstable():
    #Deze functie maak een table aan voor mijn producten die ik wil laten zien
    cur.execute("DROP TABLE IF EXISTS recomendedpro;")

    cur.execute("CREATE TABLE recomendedpro (id serial  PRIMARY KEY, "
                "_ID varchar , "
                "category varchar, "
                "sub_category varchar, "
                "targetaudience varchar, "
                "sellingprice varchar, "
                "deal varchar);")

def createrecomendeditemsrecords():
    categorydict = {}
    subcategorydict = {}
    genderdict = {}
    # met deze execute haal ik alle producten op die zowiezo een deal hebben en daarna haal ik ze gesoorteerd binnen
    cur.execute("select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products WHERE products.deal IS NOT NULL and products.category is not null order by category, subcategory, targetaudience,deal asc")
    rows = cur.fetchall()

    for row in rows:
        # een stukje code om alle categories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[1][0]], str) == True:
            if row[1] in categorydict:
                categorydict[row[1]] += 1
            else:
                categorydict[row[1]] = 1
        if row[1] in categorydict:
            categorydict[row[1]] += 1
        else:
            categorydict[row[1]] = 1

        # een stukje code om alle subcategories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[2][0]], str) == True:
            if row[2] in subcategorydict:
                subcategorydict[row[2]] += 1
            else:
                subcategorydict[row[2]] = 1
        if row[2] in subcategorydict:
            subcategorydict[row[2]] += 1
        else:
            subcategorydict[row[2]] = 1

        # een stukje code om alle genders/targetaudience uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[3][0]], str) == True:
            if row[3] in genderdict:
                genderdict[row[3]] += 1
            else:
                genderdict[row[3]] = 1
        if row[3] in genderdict:
            genderdict[row[3]] += 1
        else:
            genderdict[row[3]] = 1

    #een stukje code om de keys van alles dicts om te zetten naar een list omdat ik dat makelijker werken vindt
    categorylst = []
    subcategorylst = []
    genderlst = []
    for keys in categorydict.keys():
        categorylst.append(keys)
    for keys in subcategorydict.keys():
        subcategorylst.append(keys)
    for keys in genderdict.keys():
        genderlst.append(keys)

    #return alle list zodat ik ze ergens anders kan gebruiken in anderen stukken code voor flexibiliteit
    return categorylst,subcategorylst,genderlst

def fillrecomendeditems(categorylst,subcategorylst,genderlst):
    cur.execute("select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products WHERE products.deal IS NOT NULL and products.category is not null order by category, subcategory, targetaudience,deal asc")
    rows = cur.fetchall()
    #in dit stukje code maak ik per subcategory een selectie van 5 items per target/gender en schrijf dit weg naar de database
    for j in range(0, len(subcategorylst)):
        for k in range(0, len(genderlst)):
            #de counter voor het maximale aantal elementen per subcategory en target/gender
            count = 0
            for row in rows:
                # De i heeft de category waarmee we gaan sorteren
                if count == 5:
                    break
                if (subcategorylst[j] in row and genderlst[k] in row):
                    count += 1
                    cur.execute(
                        "INSERT INTO recomendedpro (_ID, category, sub_category, targetaudience, sellingprice, deal) VALUES ( %s, %s, %s, %s, %s, %s)",
                        (row[0], row[1], row[2], row[3], row[4], row[5]))

    for i in range(0, len(categorylst)):
    # in dit stukje code maak ik per category een selectie van 5 items per target/gender en schrijf dit weg naar de database
        for k in range(0, len(genderlst)):
            # de counter voor het maximale aantal elementen per category en target/gender
            count = 0
            for row in rows:
                # De i heeft de category waarmee we gaan sorteren
                if count == 5:
                    break
                if (subcategorylst[i] in row and genderlst[k] in row):
                    # print(row)
                    count += 1
                    cur.execute(
                        "INSERT INTO recomendedpro (_ID, category, sub_category, targetaudience, sellingprice, deal) VALUES ( %s, %s, %s, %s, %s, %s)",
                        (row[0], row[1], row[2], row[3], row[4], row[5]))

    cur.execute("select distinct recomendedpro._id, recomendedpro.category, recomendedpro.sub_category, recomendedpro.targetaudience from recomendedpro order by recomendedpro._id asc")
    prorows = cur.fetchall()
    #omdat ik problemen had met duplicate records door mijn code hierboven, besloot ik een filter select te gebruiken en de table opnieuw aantemaken zodat ik correcte waardens had
    cur.execute("DROP TABLE IF EXISTS recomendedpro;")

    cur.execute("CREATE TABLE recomendedpro (_ID varchar  PRIMARY KEY, "
                "category varchar, "
                "sub_category varchar, "
                "targetaudience varchar);")
    #Het opnieuw wegschrijven van de regels
    for prorow in prorows:
        cur.execute("INSERT INTO recomendedpro (_ID, category, sub_category, targetaudience) VALUES ( %s, %s, %s, %s)",
                    (prorow[0], prorow[1], prorow[2], prorow[3]))

    return

def getitemrecords(id):
    #het ophalen van de prodcuct gegevens met een query
    cur.execute("select products.id, products.category, products.subcategory, products.targetaudience from products where id = '{}'".format(id))
    info = cur.fetchall()
    return info

conn = psycopg2.connect("dbname=voordeelopdracht user=postgres password=kip")
cur = conn.cursor()

createrecomendeditemstable()

searchitems = createrecomendeditemsrecords()

fillrecomendeditems(searchitems[0],searchitems[1],searchitems[2])

itemrecords = getitemrecords(9196)   #Het gene wat hier in haakjes staat
print("Het ingevulde ID", itemrecords[0][0])
recomendedlist = recomendeditems(itemrecords[0][1],itemrecords[0][2],itemrecords[0][3])

#Deze for statement is zeer handig en heb ik van: https://stackoverflow.com/questions/30062429/python-how-to-get-every-first-element-in-2-dimensional-list/30062458
print("list met recomende id's",[i[0] for i in recomendedlist])

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
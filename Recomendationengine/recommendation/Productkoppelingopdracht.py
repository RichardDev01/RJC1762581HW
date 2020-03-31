#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html
import psycopg2

#not used
def recomendeditems(category,subcategory,targetaudience):
    #Hier maak ik gebruik van een SQL statement die in mijn Recomended items table alleen maar de producten hallen die overeen komen de gegeven category, subcategory en target audience(kunnen maximaal 5 items zijn*)
    #Ik moest verschillenden entries aanpassen omdat ze niet 1 op 1 in sql konden, hier onder worden de strings aangepast zodat ze werken in SQL
    if targetaudience == "Baby's":
        targetaudience = "Baby\''s"
    if subcategory == "Baby's en kinderen":
        subcategory = "Baby\''s en kinderen"
    if category == "['Make-up & geuren', 'Make-up', 'Nagellak']":
        category ="[\''Make-up & geuren\'', \''Make-up\'', \''Nagellak\'']"

    cur.execute("select recomendedpro._id, recomendedpro.category, recomendedpro.sub_category, recomendedpro.targetaudience from recomendedpro  where category = '{}'and sub_category = '{}' and targetaudience = '{}'".format(category, subcategory, targetaudience))
    info = cur.fetchall()

    return info

#not used
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
    subsubcategorydict = {}
    branddict = {}
    genderdict = {}
    # met deze execute haal ik alle producten op die zowiezo een deal hebben en daarna haal ik ze gesoorteerd binnen
    cur.execute("select all_p._id, all_p.category, all_p.sub_category, all_p.gender, all_p.sub_sub_category, all_p.brand,all_p.price, all_p.discount from all_p WHERE all_p.discount IS NOT NULL and all_p.category is not null order by category, sub_category, gender,discount asc")
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

        # een stukje code om alle subsubsubcategories uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[4][0]], str) == True:
            if row[4] in subsubcategorydict:
                subsubcategorydict[row[4]] += 1
            else:
                subsubcategorydict[row[4]] = 1
        if row[4] in subsubcategorydict:
            subsubcategorydict[row[4]] += 1
        else:
            subsubcategorydict[row[4]] = 1

        # een stukje code om alle brands uit de query te hallen en dit naar een dict te zetten zodat ik weet wat ik heb
        if isinstance(row[[5][0]], str) == True:
            if row[5] in branddict:
                branddict[row[5]] += 1
            else:
                branddict[row[5]] = 1
        if row[5] in branddict:
            branddict[row[5]] += 1
        else:
            branddict[row[5]] = 1

    #een stukje code om de keys van alles dicts om te zetten naar een list omdat ik dat makelijker werken vindt
    categorylst = []
    subcategorylst = []
    subsubcategorylst = []
    brandlst = []
    genderlst = []
    for keys in categorydict.keys():
        categorylst.append(keys)
    for keys in subcategorydict.keys():
        subcategorylst.append(keys)
    for keys in genderdict.keys():
        genderlst.append(keys)
    for keys in subsubcategorydict.keys():
        subsubcategorylst.append(keys)
    for keys in branddict.keys():
        brandlst.append(keys)

    #return alle list zodat ik ze ergens anders kan gebruiken in anderen stukken code voor flexibiliteit
    return categorylst,subcategorylst,genderlst,subsubcategorylst,brandlst

#not used
def fillrecomendeditems(categorylst,subcategorylst,genderlst):
    cur.execute("select all_p._id, all_p.category, all_p.sub_category, all_p.gender, all_p.price, all_p.discount from all_p WHERE all_p.discount IS NOT NULL and all_p.category is not null order by category, sub_category, gender,discount asc")
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

#not used
def getitemrecords(id):
    #het ophalen van de prodcuct gegevens met een query
    #filter voor een specifieke record
    if id == "38647-It'sglowtime":
        id = "38647-It\''sglowtime"
    cur.execute("select all_p._id, all_p.category, all_p.sub_category, all_p.gender from all_p where _id = '{}'".format(id))
    info = cur.fetchall()
    return info

#not used
def createidlink():
    #een functie om een tabel aan temaken
    cur.execute("DROP TABLE IF EXISTS prolink;")

    cur.execute("CREATE TABLE prolink (PID varchar  PRIMARY KEY, "
                "pro1 varchar, "
                "pro2 varchar, "
                "pro3 varchar, "
                "pro4 varchar, "
                "pro5 varchar);")
    return
#not used
def fillidlinktable():
    #Deze functie itereerd over alle items die er zijn en verwerkt alleproducten in een nieuwe tabel met de recommended items erbij
    cur.execute("select all_p._id from all_p")
    ids = cur.fetchall()

    for id in ids:
        itemrecords = getitemrecords(id[0])
        recomendedlist = recomendeditems(itemrecords[0][1], itemrecords[0][2], itemrecords[0][3])
        #print("list met recomende id's", [i[0] for i in recomendedlist])
        if len(recomendedlist) == 5:
            cur.execute("INSERT INTO prolink (PID, pro1, pro2, pro3,pro4,pro5) VALUES ( %s, %s, %s, %s,%s,%s)",(id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0],recomendedlist[3][0],recomendedlist[4][0]))
        if len(recomendedlist) == 4:
            cur.execute("INSERT INTO prolink (PID, pro1, pro2, pro3,pro4) VALUES ( %s, %s, %s, %s,%s)",(id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0],recomendedlist[3][0]))
        if len(recomendedlist) == 3:
            cur.execute("INSERT INTO prolink (PID, pro1, pro2, pro3) VALUES ( %s, %s, %s, %s)",(id, recomendedlist[0][0], recomendedlist[1][0], recomendedlist[2][0]))
        if len(recomendedlist) == 2:
            cur.execute("INSERT INTO prolink (PID, pro1, pro2) VALUES ( %s, %s, %s)",(id, recomendedlist[0][0], recomendedlist[1][0]))
        if len(recomendedlist) == 1:
            cur.execute("INSERT INTO prolink (PID, pro1) VALUES ( %s, %s)",(id, recomendedlist[0][0]))
        if len(recomendedlist) == 0:
            cur.execute("INSERT INTO prolink (PID) VALUES ( %s)",(id))
    print("finnisched filling product table")
    return

#not used
def getsegmenttypes():
    #Hier heb ik een stukje code om ale segments te fetchen en te verwerken zodat ik mijn code zo flexibel mogelijk heb
    #ik heb hier de records op maximaal 10000 staan vanwegen snelheid
    segmentdict= {}
    cur.execute("select sessions.profid, sessions.segment,sessions.sale,profiles_previously_viewed.prodid, products.category, products.subcategory, products.targetaudience from sessions right JOIN profiles_previously_viewed ON sessions.profid=profiles_previously_viewed.profid right JOIN products ON products.id=profiles_previously_viewed.prodid limit 10000")
    getsegments= cur.fetchall()
    #print(getsegments)
    for segment in getsegments:
        #print(segment[1])
        if segment[1] in segmentdict:
            segmentdict[segment[1]] += 1
        else:
            segmentdict[segment[1]] = 1

    #Het aanmaken van een tabel voor het uiteindelijk resultaat
    cur.execute("DROP TABLE IF EXISTS segmenttocat; CREATE TABLE segmenttocat (segment VARCHAR, category VARCHAR, PRIMARY KEY (segment)); ")
    #Hier maak ik gebruik van een sql statement om een nieuwe table aan temaken om me verder tewerken voor de gemakelijkheid
    cur.execute("DROP TABLE IF EXISTS combindedsession; CREATE TABLE combindedsession AS select sessions.profid, sessions.segment,sessions.sale,profiles_previously_viewed.prodid, products.category, products.subcategory, products.targetaudience from sessions  right JOIN profiles_previously_viewed ON sessions.profid=profiles_previously_viewed.profid right JOIN products ON products.id=profiles_previously_viewed.prodid order by prodid asc limit 10000;")

    i=0
    for keys in segmentdict.keys():

        maxrecord = {}
        cur.execute("Select distinct prodid from combindedsession where segment = '{}'".format(list(segmentdict.keys())[i]))
        products = cur.fetchall()
        for producten in products:

            #Ik maak gebruik van de eigenschappen van een dictionaire om de records te tellen zodat ik weet wat een segments het meeste koopt en daarop kan baseren wat hij/zij aangeraden moet krijgen
            record = getitemrecords(producten[0])[0][1]
            if record in maxrecord:
                maxrecord[record] += 1
            else:
                maxrecord[record] = 1

        v = list(maxrecord.values())
        k = list(maxrecord.keys())
        #door onregelmatige data kan het voorkomen dat het niet altijd goed gaat, daarm een try except
        try:
            mostcat = k[v.index(max(v))]
        except:
            i += 1
            continue
        cur.execute("INSERT INTO segmenttocat (segment,category) VALUES ( %s,%s)", (keys,mostcat))
        i+=1

    print("finished maken segment to category")
    return

def clearerd():
    cur.execute("DROP TABLE category CASCADE;")
    cur.execute("DROP TABLE gender CASCADE;")
    cur.execute("CREATE TABLE category (idcatergory serial NOT NULL,category varchar(45),sub_category varchar(45),sub_sub_category varchar(45),CONSTRAINT category_pk PRIMARY KEY (idcatergory)) WITH (OIDS=FALSE);")
    cur.execute("CREATE TABLE gender (idgender serial NOT NULL,gendernaam varchar(45),CONSTRAINT gender_pk PRIMARY KEY (idgender)) WITH (OIDS=FALSE);")
    cur.execute("INSERT INTO category(category,sub_category,sub_sub_category) SELECT DISTINCT category, sub_category,sub_sub_category from all_p order by category asc;")
    return

conn = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")
cur = conn.cursor()

#~~~~~~~~~~~~~~~~~~~~~~~~ code voor product koppeling
#createrecomendeditemstable()

searchitems = createrecomendeditemsrecords()

clearerd()

#print("cat", searchitems[0],"\n")
#print("subcat",searchitems[1],"\n")
#print("gender",searchitems[2],"\n")
#print("subsubcat", searchitems[3],"\n")
#print("brand",searchitems[4],"\n")

for item in searchitems[2]:
    #print(item)
    cur.execute("INSERT INTO gender(gendernaam) VALUES ('{}')".format(item))

for item in searchitems[4]:
    #print(item)
    if item == "M&M's":
        item = "M&M\''s"
    if item == "Grab 'n Go":
        item = "Grab \''n Go"
    if item == "Lucy's Home":
        item = "Lucy\''s Home"
    if item == "L'alerteur":
        item = "L\''alerteur"
    if item == "Dr. Tom's":
        item = "Dr. Tom\''s"
    if item == "Lay's":
        item = "Lay\''s"
    if item == "Tesori d'Oriente":
        item = "Tesori d\''Oriente"
    if item == "Pet's Unlimited":
        item = "Pet\''s Unlimited"
    cur.execute("INSERT INTO brand(brandnaam) VALUES ('{}')".format(item))
#fillrecomendeditems(searchitems[0],searchitems[1],searchitems[2])

#createidlink()

#fillidlinktable()

#~~~~~~~~~~~~~~~~~~~~~~~~ code voor profil koppeling
#getsegmenttypes()

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
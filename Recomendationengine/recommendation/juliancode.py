import psycopg2

def formatting_data(idbrand):
    idbrandlist = []

    for item in idbrand:
        item2 = list(item)
        idbrandlist.append(item2)

    return idbrandlist

def brandrecommendation(prodid):
    prodid = str(prodid)
    reclist = []
    prodidbrand = ""

    index = 0
    for item in ids:
        if item[0] == prodid:
            prodidbrand = item[1]
            break
        index += 1

    index = 0
    for item in ids:
        if item[1] == prodidbrand:
            reclist.append(item[0])

    if len(reclist) >= 5:
        c.execute("INSERT INTO brandrecommendations (prodid, product1, product2, product3, product4, product5) VALUES (%s, %s, %s, %s, %s, %s)", (
        id, reclist[0], reclist[1], reclist[2], reclist[3], reclist[4]))
    if len(reclist) == 4:
        c.execute("INSERT INTO brandrecommendations (prodid, product1, product2, product3, product4) VALUES ( %s, %s, %s, %s,%s)",
                    (id, reclist[0], reclist[1], reclist[2], reclist[3]))
    if len(reclist) == 3:
        c.execute("INSERT INTO brandrecommendations (prodid, product1, product2, product3) VALUES ( %s, %s, %s, %s)",
                    (id, reclist[0], reclist[1], reclist[2]))
    if len(reclist) == 2:
        c.execute("INSERT INTO brandrecommendations (prodid, product1, product2) VALUES ( %s, %s, %s)",
                    (id, reclist[0], reclist[1]))
    if len(reclist) == 1:
        c.execute("INSERT INTO brandrecommendations (prodid, product1) VALUES ( %s, %s)", (id, reclist[0]))
    if len(reclist) == 0:
        c.execute("INSERT INTO brandrecommendations (prodid) VALUES ( %s)", (id))
    return

connect = psycopg2.connect("dbname=voordeelshoponescript user=postgres password=kip")
c = connect.cursor()
print("postgres connected")

c.execute("DROP TABLE IF EXISTS brandrecommendations CASCADE")
c.execute("CREATE TABLE brandrecommendations (prodid VARCHAR PRIMARY KEY, "
          "product1 VARCHAR, product2 VARCHAR, product3 VARCHAR, product4 VARCHAR, product5 VARCHAR);")

c.execute("select id, brand_idbrand from product")
ids = c.fetchall()

counter = 0

for id in ids:
    brandrecommendation(id[0])
    counter += 1
    if counter % 1000 == 0:
        print(counter)

print("table filled")

c.close()
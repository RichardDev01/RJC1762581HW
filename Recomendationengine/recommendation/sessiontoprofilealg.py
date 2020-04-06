import psycopg2

conn = psycopg2.connect("dbname=voordeelschoptest user=postgres password=kip")
cur = conn.cursor()

#cur.execute("select buid,id,itorder from session where itorder != '{}' and buid != 'null'")
cur.execute("select * from session")
buids = cur.fetchall()
for buid in buids:
    print(list(buid))

profid = 0
sesid = 0
count = 0
'''
for buid in buids[:250]:
    # print(buid[0][2:-2])
    cur.execute("SELECT id FROM profile WHERE buids like ('%{}%')".format(buid[0][2:-2]))
    try:
        profid = cur.fetchall()[0][0]
        sesid = buid[1]
        # print("profid",profid)
        # print("id",sesid)
        cur.execute("UPDATE session SET profile_id = '{}' WHERE id = '{}';".format(profid, sesid))
        cur.execute("UPDATE profile SET recommendations = '{}' WHERE id = '{}';".format(buid[2], buid[1]))
    except:
        print("Error", "profid", profid, "id", sesid)
        # print("id",sesid)
    count += 1
    if count % 50 == 0:
        print(count, "profiles linked")
'''
print("done with profile-link")
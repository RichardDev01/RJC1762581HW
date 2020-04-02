import psycopg2
connect = psycopg2.connect("dbname=voordeelshopgp user=postgres password=kip")
cur = connect.cursor()

cur.execute("SELECT * FROM SESSION WHERE profile_id != 'null'")
idsfromses = cur.fetchall()
cur.execute("SELECT * FROM PROFILE")
ids = cur.fetchall()

print(idsfromses)
print("-------------------------------------------------------------------")
print(ids)
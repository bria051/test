import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("select * from shopping_list where ID = 'at01'")

rows = cur.fetchall()
for row in rows:
    print(row)


conn.close()


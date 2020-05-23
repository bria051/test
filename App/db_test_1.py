import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE shopping_list(ID text, PWD text)")
# cur.execute("CREATE TABLE sign_in(ID test PRIMARY KEY , PW text, Name text, Age int)")

conn.commit()
conn.close()
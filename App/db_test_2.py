import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

try:
    # cur.execute("INSERT INTO turing VALUES('namgil', 'hello')")
    # cur.execute("CREATE TABLE kakao(ID test PRIMARY KEY , PW text)")
    cur.execute("INSERT INTO sign_in VALUES('at01', '1234')")

    conn.commit()
    conn.close()
except:
    print("not execute")
    conn.close()
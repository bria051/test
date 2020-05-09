#DATABASE
import sqlite3
from flask import Flask, render_template, redirect, request, url_for

conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS shopping (item TEXT, num TEXT, price TEXT)')
print("Table created successfully")
conn.close()

col = sqlite3.connect('login_id_pass.db')
print("Opened database successfully")
col.execute('CREATE TABLE IF NOT EXISTS shopping (id TEXT, password TEXT)')
print("Table created successfully")
col.close()

app = Flask(__name__)

@app.route('/')
def hi():
    return "hello"

"""
@app.route('/logout')
def logout():
    f = open("./test.txt", 'w')
    f.close()
    return redirect(url_for('login'))

def id(username, password):
    id_box = {'apple': '1234', 'banana': '5678', 'orange': '0000'}
    if id_box.get(username) == password:
        f = open("./test.txt", 'w')
        f.write("login")
        f.close()

        return None
    elif id_box.get(username) == None:
        return "Username Unfounded"
    else:
        return "Wrong password"

@app.route('/login', methods=['GET', 'POST'])
def login():
    f = open("test.txt", 'r')
    tf = f.readline()
    f.close()

    if tf == "login":
        return redirect(url_for('shopping'))

    error = None
    if request.method == 'POST':
        error = id(request.form['username'],request.form['password'])
        if error == None:
            return redirect(url_for('shopping'))
    return render_template('login.html', error=error)
"""

@app.route('/login_page', methods = ['POST', 'GET'])
def login_page():
    con = sqlite3.connect("login_id_pass.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()

    msg = ""
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        for row in rows:
            if row["id"] == id and row["password"] == password:
                return redirect(url_for('shopping'))
    return render_template('id_password.html')




@app.route('/shopping')
def shopping():

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    for row in rows:
        print(row["item"], row["num"], row["price"])
    print("DB:")
    print(rows)
    return render_template('sh_list.html', rows = rows)




@app.route('/database_add', methods = ['POST', 'GET'])
def database_add():
    msg = ""
    if request.method == 'POST':
        try:
            item = request.form['item']
            num = request.form['num']
            price = request.form['price']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO shopping (item, num, price) VALUES (?, ?, ?)", (item, num, price))
                con.commit()
                msg = "sucees"
                con.close()
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("shopping_add_result.html", message=msg)


if __name__ == '__main__':
    app.run()
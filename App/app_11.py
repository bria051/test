from flask import Flask, render_template, redirect, request, url_for, session
import sqlite3
from App import app_9

app = Flask(__name__)

app.secret_key = "namgil"

app_9.save_id = None

@app.route('/')
def lobby():
    return "Hello, world"

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    conn = sqlite3.connect("test.db")

    cur = conn.cursor()

    error = None
    if request.method == 'POST':
        try:
            print(request.form['ID'], request.form['pass'], request.form['name'], request.form['age'])
            command = "INSERT INTO sign_in VALUES('{}', '{}', '{}', {})".format(request.form['ID']
                                    , request.form['pass'],request.form['name'], request.form['age'])
            print(command)
            cur.execute(command)

            conn.commit()
            conn.close()
            return redirect(url_for('lobby'))
        except:
            error = "not execute"
            conn.close()


    return render_template('sign_in_page.html', error=error)

@app.route('/basket', methods=['GET', 'POST'])
def basket():
    conn = sqlite3.connect("test.db")

    cur = conn.cursor()

    error = None
    if request.method == 'POST':
        try:
            cur.execute("INSERT INTO shopping_list VALUES('{}', '{}')".format(app_9.save_id, request.form['basket']))

            conn.commit()
            conn.close()
            error = "added"
            return render_template('basket.html', error=error)
        except:
            error = "not execute"
            conn.close()

    return render_template('basket.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = sqlite3.connect("test.db")

    cur = conn.cursor()

    error = None
    if request.method == 'POST':
        try:
            lg_id = request.form['username']
            lg_pass = request.form['password']

            cur.execute("select * from sign_in where ID = '{}'".format(lg_id))
            rows = cur.fetchall()

            for row in rows:
                id, password, name, age = row
                if password == lg_pass:
                    app_9.save_id = lg_id
                    return redirect(url_for('basket'))

                else:
                    error = "can't login"
            conn.close()
        except:
            error = "id not found"
            conn.close()

    return render_template('login_1.html', error=error)



if __name__ == '__main__':
    f = open('./test.txt', 'w')
    app.run()






















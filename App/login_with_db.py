from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3


conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS shopping (item TEXT, num TEXT, price TEXT)')
print("Table created successfully")
conn.close()

app = Flask(__name__)

app.secret_key = 'b_1234abc'


conn = sqlite3.connect("user.db")

cur = conn.cursor()

try:
    cur.execute("CREATE TABLE namgil(ID text, PWD text)")
    conn.commit()
    conn.close()
except:
    print("already db")

# @app.route('/')
# def main():
#     return redirect(url_for('login'))
@app.route('/')
def main():
    return render_template('main.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if not session.get('logged_in'):
        if request.method == 'POST':
            con = sqlite3.connect("user.db")
            cur = con.cursor()
            login_id = request.form.get('id', "not data")
            login_pwd = request.form.get('pwd', "not data")
            if login_id == "not data":
                return render_template('login.html')

            execute = "SELECT * FROM namgil where id =(?)"
            cur.execute(execute, [login_id])
            rows = cur.fetchall()
            con.commit()
            con.close()

            try:
                if rows[0][1] == login_pwd:
                    print("Success Login")
                    session['logged_in'] = True
                    return redirect(url_for('addrec'))
            except:
                print("Fail Login")
                return render_template('login.html')

    else:
        return redirect(url_for('addrec'))
    return render_template('login.html', error=error)

@app.route("/sign_up/", methods=['POST'])
def sign_up():

    if request.method == 'POST':
        con = sqlite3.connect("user.db")
        cur = con.cursor()

        want_id = request.form.get('want_id', "not data")
        want_pwd = request.form.get('want_pwd', "not data")

        if want_id == "not data":
            return render_template('join.html')
        execute = "INSERT INTO namgil(ID, PWD)VALUES(?,?)"
        cur.execute(execute, (want_id, want_pwd))
        print("Success Join")
        try:
            con.commit()
            con.close()
            return redirect(url_for('login'))
        except:
            print("Fail Join")
            return render_template('join.html')
    else:
        return render_template('join.html')



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/shopping', methods=['POST'])
def shopping():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from shopping")
    rows = cur.fetchall()
    print("DB:")
    print(rows)
    return render_template('sh_list.html', rows = rows)

@app.route('/addrec', methods = ['POST', 'GET'])
def addrec():
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
                msg = "Recode successfully added"
                return render_template("shopping_add_result.html", message=msg)
        except:
            con.rollback()
            msg = "Error in insert operation"
            return render_template("shopping_add_result.html", message=msg)
    else:
        msg = ""
        return render_template("shopping_add_result.html", message=msg)


if __name__ == '__main__':
    app.run()



from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

def check(username, password):
    id_box = [('apple', '1234'), ('banana', '5678'), ('orange', '0000')]
    for x, y in id_box:
        if username == x:
            if password == y:
                return None
            else:
                return "Wrong password"
    return "Username Unfounded"

def id(username, password):
    id_box = {'apple': '1234', 'banana': '5678', 'orange': '0000'}
    if id_box.get(username) == password:
        return None
    elif id_box.get(username) == None:
        return "Username Unfounded"
    else:
        return "Wrong password"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        error = id(request.form['username'],request.form['password'])
        if error == None:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

"""
def check(username, password):
    id_box = [('apple', '1234'), ('banana', '5678'), ('orange', '0000')]
    for x, y in id_box:
        if username == x:
            if password == y:

                return None
            else:
                return "Wrong password"
    return "Username Unfounded"
"""


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


def multiple(num):
    sentence = ""
    for x in range(1, 10):
        sentence += "%d x %d = %d\n"%(num, x, num*x)
    print(sentence)
    return sentence


@app.route('/')
def home():
    return "Hello, world"


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    value = None
    if request.method == 'POST':
        form = int(request.form['calculate'])

    return render_template('welcome.html', value=value)


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    multi = None
    if request.method == 'POST':
        number = int(request.form['number'])
        multi = int(number)
    return render_template('welcome.html', num=multi)


@app.route('/logout')
def logout():
    f = open("./test.txt", 'w')
    f.close()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    f = open("test.txt", 'r')
    tf = f.readline()
    f.close()

    if tf == "login":
        return redirect(url_for('welcome'))

    error = None
    if request.method == 'POST':
        error = id(request.form['username'],request.form['password'])
        if error == None:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
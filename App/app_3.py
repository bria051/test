from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def helloworld(num=None):
    return render_template('intro_3.html', num=num)

@app.route('/cal', methods=['POST'])
def namgil():
    temp = request.form['num']
    if request.method == 'POST':
        print(request.method)
        return redirect(url_for('helloworld', num=temp))

@app.route('/ll')
def ll():
    return "tada"

if __name__ == '__main__':
    app.run()
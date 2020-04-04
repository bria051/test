from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/easter_egg')
def hello():
    return "you found it"

@app.route('/n')
def default_function():
    return "default"

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def home():
    path = "/home/at02/PycharmProjects/brian/App/static"
    file_list = os.listdir(path)
    x = random.randrange(1, len(file_list))
    return render_template('img_static.html', image=file_list[x])

if __name__ == "__main__":
    app.run()
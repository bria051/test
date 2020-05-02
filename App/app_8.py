from flask import Flask, render_template, redirect, request, url_for, session
import os
import shutil

first = "/home/at02/PycharmProjects/brian/App"
mid_1 = "/images/"
mid_2 = "/static/"
last = ".png"


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def image_select():
    if request.method == 'POST':
        image = request.form['season']
        if os.path.isfile(first + mid_1 + image + last):
            image += last
            return render_template('img_static.html', image=image)
        else:
            if os.path.isfile(first + mid_2 + image + last):
                shutil.copy(first + mid_2 + image + last, first + mid_1 + image + last)
            else:
                image = None
            return render_template('img_static.html', image=image)

    else:
        return render_template('img_select.html')

if __name__ == "__main__":
    app.run()
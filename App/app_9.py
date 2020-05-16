from flask import Flask, render_template, redirect, request, url_for, session
import os
import shutil

# homework hint: cv2



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def image_select():
    if request.method == 'POST':
        pass
    else:
        return render_template('img_select.html')

if __name__ == "__main__":
    app.run()

save_id = None
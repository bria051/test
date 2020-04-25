from flask import  Flask, render_template

app = Flask(__name__)

temp_list = ["alpha","beta","gamma","delta","epsilon","zeta","eta","theta","iota","kappa"]

@app.route('/')
def default_function():
    return render_template('for_loop.html', len=len(temp_list), temp_list=temp_list)

if __name__ == '__main__':
    app.run()
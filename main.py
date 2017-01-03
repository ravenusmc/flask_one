from flask import Flask, render_template, request
from one import *
import time

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', the_title='Home Page')

@app.route('/one', methods=['POST'])
def first():
    num1 = int(request.form['numberOne'])
    num2 = int(request.form['numberTwo'])
    return str(num(num1, num2))

@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Mikes Math Site')

app.run(debug=True)


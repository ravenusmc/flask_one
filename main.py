from flask import Flask, render_template, request
from one import *
import time

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', the_title='Home Page')

#Code for addition pages
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Mikes Math Site')

@app.route('/one', methods=['POST'])
def first():
    numOne = int(request.form['numberOne'])
    numTwo = int(request.form['numberTwo'])
    results = str(num(numOne, numTwo))
    return render_template('results.html', numOne = numOne, numTwo = numTwo, result = results)

#Code for multiplication pages
@app.route('/multiply')
def multiply_page():
    return render_template('times.html', the_title='Multiply Time!')


#NEED TO MAKE ONE FINAL SET OF PAGES FOR USERS NAME

app.run(debug=True)

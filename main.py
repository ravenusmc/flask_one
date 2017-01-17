from flask import Flask, render_template, request
from one import *
from times import *
from names import *
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

@app.route('/times', methods=['POST'])
def second():
    first = int(request.form['numOne'])
    second = int(request.form['numTwo'])
    answer = str(times(first, second))
    return render_template('mul_results.html', result = answer, one = first, two = second)

#Code for name pages
@app.route('/name')
def name_page():
    return render_template('name.html', the_title='Name Time!')

@app.route('/names', methods=['POST'])
def third():
    first = str(request.form['first'])
    last = str(request.form['last'])
    full_name = str(name(first, last))
    return render_template('name_results.html', full = full_name, first = first, last = last)

app.run(debug=True)

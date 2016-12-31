from flask import Flask, render_template
from one import *

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World'

@app.route('/entry')
def entry_page():
  return render_template('entry.html', the_title='Mikes Math Site')

# @app.route('/one')
# def first():
#   return str(num(2,3))

app.run(debug=True)

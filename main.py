from flask import Flask
from one import *

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World'

@app.route('/one')
def first():
  return str(num(2,3))

app.run()

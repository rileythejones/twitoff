"""Minimal flask app"""

from flask import Flask 

# make app
app = Flask(__name__)


# make route
@app.route("/")

# now define a function 
def hello:
    return "hello world!"
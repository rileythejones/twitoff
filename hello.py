"""Minimal flask app"""

from flask import Flask, render_template



# make app
app = Flask(__name__)


# make route
@app.route("/")
# now define a function 
def hello():
    return render_template('home.html')

# make a second route 
@app.route("/about")
# make the function that goes with about 
def preds():
    return render_template('about.html')
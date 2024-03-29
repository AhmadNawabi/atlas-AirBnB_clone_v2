#!/usr/bin/python3
"""import flask from python librarry"""
from flask import Flask
"""store the flask to the app variable"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Define the route (/) to display Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define the route(/hbnb) to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cIsFun(text):
    """Define the (/c/<text>) to desplay text"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyhtonIsCool(text="is cool"):
    """Define the pytonIsCool to dispaly the text"""
    return "Pyhton " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def isInteger(n):
    """Define isInteger"""
    """return 'n is a number only if n is integer'"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    """Run app to host=0.0.0.0 and port=5000"""
    app.run(host="0.0.0.0", port=5000)

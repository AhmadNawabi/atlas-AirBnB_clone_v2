#!/usr/bin/python3

"""import flask from python librarry"""
from flask import Flask
"""store flask into app variable"""
app = Flask(__name__)


@app.route("/",  strict_slashes=False)
def hello():
    """Define a route for the root URL
    ("/") with strict_slashes=false"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Define a route for the root URL
    ("/HBNB") with strict_slashes=false"""
    return "HBNB"


if __name__ == "__main__":
    """Run flask in host=0.0.0.0 and port=5000"""
    app.run(host='0.0.0.0', port=5000)

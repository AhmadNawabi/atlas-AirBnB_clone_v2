#!/usr/bin/python3
"""import flask from python librarry"""
from flask import Flask
"""store flask into app variable"""
app = Flask(__name__)
"""Define a route for the root URL
("/") with strict_slashes=false"""


@app.route("/",  strict_slashes=False)
def hello():
    return "Hello HBNB"


if __name__ == "__main__":
    """Run flask in host=0.0.0.0 and port=5000"""
    app.run(host='0.0.0.0', port=5000)

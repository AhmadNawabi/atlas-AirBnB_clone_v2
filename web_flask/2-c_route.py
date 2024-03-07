#!/usr/bin/python3

"""import flask from python librarry"""
from flask import Flask

"""store the flask into app variable"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Define the route (/) to display Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define the route (/hbnb) to display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text():
    """Define route (/c/<text>"""
    """Replace the ("_" with "" space)"""
    text_format = text.replace("_", " ")
    return f"C {text_format}"


if __name__ == "__main__":
    """Run the app to host=0.0.0.0 and port=5000"""
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3

"""import the flask from python library"""
from flask import Flask

"""Create a app variable and store the flask"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Define route (/) to display Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Define the (/hbnb) route to display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_display(text):
    """define the (/c/<text>) route to display text"""
    """Replace the _ with space in text"""
    formated_text = text.replace("_", " ")
    return f"C {formated_text}"


@app.route("/python/<text>", strict_slashes=False)
def python_display(text="is cool"):
    """Define the (/python/<text>) to display the text"""
    """Replace the _ with space in text"""
    text_formated = text.replace("_", "")
    return f"Python {text_formated}"
 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3

"""import flask and render_template to start 
   Flask application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cIsFun(text):
    """Return C with the values of text"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonIsCool(text="is cool"):
    """Return Python with the value of the text"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """Return the value of the only if it is a number"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbersAndTemplate(n):
    """Return H1 tag: “Number: n” inside the tag BODY"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberOddOrEven(n):
    """Determine if the number is even or odd"""
    result = "even" if n %2 == 0 else "odd"
    """Render the template with the determined result"""
    return render_template("6-number_odd_or_even.html", n=n, result=result)


if __name__ == "__main__":
    """Run app at the host=0.0.0.0 port=5000"""
    app.run(host="0.0.0.0", port=5000)

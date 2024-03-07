"""import flask from python library"""
from flask import Flask

"""store flask in the app variable"""
app = Flask(__name__)

"""Define a route for the root URL ("/") with strict_slashes=false"""
@app.route('/')
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    """Run the flask app on 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)

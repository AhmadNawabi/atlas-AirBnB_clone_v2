#!/usr/bin/python3
"""Import the Flask class and the render_template function from the Flask module"""
from flask import Flask, render_template

"""Import the storage engine from the models module"""
from models import storage

"""Create a Flask web application instance with the current module's name as the argument"""
app = Flask(__name__)

"""Define a function to be called when the application context is torn down
This function closes the storage engine's session"""
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

"""Define a route for the URL '/cities_by_states' with the option strict_slashes set to False"""
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Get all State objects from the storage, sort them by name, and store in the 'states' variable"""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)

    """Render the 'cities_by_states.html' template, passing the 'states' variable to the template"""
    return render_template('cities_by_states.html', states=states)

"""Start the Flask application if the script is executed directly"""
if __name__ == "__main__":
    """Run the application on 0.0.0.0 (accessible from any IP) and port 5000"""
    app.run(host='0.0.0.0', port=5000)

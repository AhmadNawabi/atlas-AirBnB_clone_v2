#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Display a HTML page with a list of all State objects"""

    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session"""

    storage.close()


if __name__ == '__main__':
    # Import data dumps before running the application
    from models import db_storage

    db_storage.reload()

    app.run(host='0.0.0.0', port=5000)

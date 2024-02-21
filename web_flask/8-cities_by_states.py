#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)
    return render_template('7-states_list.html', states=states)


def cities_list():
    """a function that displays HTML page with a list cities
    ordered by states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)
    state_cities = []
    for state in states:
        state_cities.append([state, sorted(state.citites,
                                           key=lambda key: key.name)])
    return render_template('8-cities_by_states.html', states=state_cities,
                           heading="States")


@app.teardown_appcontext
def teardown_db(exception):
    """a function that closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

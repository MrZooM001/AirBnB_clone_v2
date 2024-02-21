#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_of_states():
    """a function that displays a HTML page with a list of states
    & sorted by state name in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """a function that displays HTML page with a list cities
    ordered by states"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda s: s.name)
    st_cities = []
    for state in states:
        st_cities.append([state, sorted(state.cities, key=lambda c: c.name)])
    return render_template('8-cities_by_states.html', states=st_cities,
                           heading="States")


@app.teardown_appcontext
def teardown_db(exception):
    """a function that closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

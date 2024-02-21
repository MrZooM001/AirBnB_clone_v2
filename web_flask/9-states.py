#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """a function that displays HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    state = ""
    cities = []
    found = 0
    for st in states:
        if st.id == id:
            state = st
            found = 1
            break
    if found:
        states = sorted(state.cities, key=lambda s: s.name)
        state = state.name
    if id and not found:
        found = 2
    return render_template('9-states.html',
                           state=state,
                           list=states,
                           found=found)


@app.teardown_appcontext
def teardown_db(exception):
    """a function that closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

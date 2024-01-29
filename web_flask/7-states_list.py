#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """a function that displays a HTML page with a list of states
    & sorted by state name in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db():
    """a function that closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

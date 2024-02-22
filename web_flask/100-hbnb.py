#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_live():
    """a function that displays HTML page with a list cities
    ordered by states"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda s: s.name)
    amenities = storage.all("Amenity").values()
    amenities = sorted(amenities, key=lambda a: a.name)
    st_cities = []
    for state in states:
        st_cities.append([state, sorted(state.cities, key=lambda s: s.name)])
    places = storage.all("Place").values()
    places = sorted(places, key=lambda p: p.name)
    return render_template('100-hbnb.html',
                           states=st_cities,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """a function that closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

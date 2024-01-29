#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """a function that view the root of the website"""
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """a function that view hbnb page"""
    return "<p>HBNB</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

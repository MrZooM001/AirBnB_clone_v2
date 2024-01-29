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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """a function that view c page with a text"""
    return "<p>C {}</p>".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """a function that view python page with a text"""
    return "<p>Python {}</p>".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_number(n):
    """a function that view number page with a number"""
    return "<p>{:d} is a number</p>".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbersandtemplates(n):
    """a function that only view HTML page if n is a number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numbersandevenness(n):
    """a function that only view HTML page if n is an integer & parity type"""
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return render_template("6-number_odd_or_even.html", n=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

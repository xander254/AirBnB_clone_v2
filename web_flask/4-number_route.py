#!/usr/bin/python3
"""
A module that runs a flask route
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A method to return hello from hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A route that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """
    A route that display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return "C " + text.replace("_", " ")


@app.route(
    "/python/",
    defaults={"text": "is cool"},
    strict_slashes=False
)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    A route to display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

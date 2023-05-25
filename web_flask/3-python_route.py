#!/usr/bin/python3
"""
A simple flask server model with one route
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    The index route returning Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    The hbnb route returning HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    C route that returns C and the text
    """
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Python route prints python and text

    Args:
    text: a string to add to python
    """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""
A simple flask server module containing routes
for web framework tasks
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3

"""
Start a flask application
and greet the user.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Greet the user."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display HBNB."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display text"""
    return "C {}".format(
            text.replace('_', ' ') if '_' in text else text
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

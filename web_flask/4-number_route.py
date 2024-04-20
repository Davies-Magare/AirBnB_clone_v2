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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_what(text="is cool"):
    """Python is Cool"""

    return "Python {}".format(
            text.replace('_', ' ') if '_' in text else text
    )


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """Display an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

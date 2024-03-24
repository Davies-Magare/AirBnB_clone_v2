#!/usr/bin/python3
"""Hello hbnb route and view function"""
from flask import Flask
app = Flask(__name__)
app.config['strict_slashes'] = False


@app.route('/')
def hello_hbnb():
    """Display greeting"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb_2():
    """Define route for /hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def what_is_c(text):
    """Define route for /c/<text"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cooler(text='is cool'):
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

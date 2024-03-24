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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

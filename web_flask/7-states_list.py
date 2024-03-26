#!/usr/bin/python3
"""Hello hbnb route and view function"""
from flask import Flask, render_template
app = Flask(__name__)
app.config['strict_slashes'] = False

from models import storage
from models.state import State
states = storage.all(State)
states_list = []
for key, value in states.items():
    states_list.append(value)
sorted_states = sorted(states_list, key = lambda x: x.name)

#@app.teardown_appcontext
#def remove_session(storage):
#     storage.close()

@app.route('/states_list')
def display_states():
    """Display states in the database."""
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
'''starts a Flask web application
must be listening on 0.0.0.0, port 5000
display a HTML page with list of states'''

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exception=None):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    '''lists states objects in database'''
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_of_state():
    '''lists cities by the states'''
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

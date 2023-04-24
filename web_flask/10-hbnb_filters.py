#!/usr/bin/python3
"""Script that runs a Flask web application"""

import os
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_city(id=None):
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

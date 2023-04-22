#!/usr/bin/python3
'''starts a Flask web application
must be listening on 0.0.0.0, port 5000
/: display “Hello HBNB!”
/hbnb: display “HBNB”'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    '''returns a string Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''returns a string "hbnb"'''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

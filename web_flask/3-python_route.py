#!/usr/bin/python3
"""
Starting Flask Web application
listening on 0.0.0.0, port 5000
Routes : /: display “Hello HBNB!”
         /hbnb: display “HBNB”
         /c/<text>: display “C ” followed by the value of the text
         variable
         /python/(<text>):display “Python ”,
         followed by the value of the text variable
         The default value of text is “is cool”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """"""
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text="is cool"):
    """"""
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

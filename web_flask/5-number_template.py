#!/usr/bin/python3
"""
Starting Flask Web application
listening on 0.0.0.0, port 5000
Routes : /: display “Hello HBNB!”
         /hbnb: display “HBNB”
         /c/<text>: display “C ” followed by the value of the text
         variable
         /python/(<text>):display “Python ”, followed by the value of the text variable
         The default value of text is “is cool”
         /number/<n>: display “n is a number” only if n is an integer
         /number_template/<n>: display a HTML page only if n is an integer:
         h1 tag: “Number: n” inside the tag body
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text="is cool"):
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n=None):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

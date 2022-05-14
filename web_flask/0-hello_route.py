#!/usr/bin/python3
"""
Starting Flask Web application
listening on 0.0.0.0, port 5000
Route : /: display “Hello HBNB!”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route : /: display “Hello HBNB!”"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

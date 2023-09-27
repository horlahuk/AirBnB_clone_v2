#!/usr/bin/python3
'''starts a flask web app'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet():
    '''display hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''display c followed by param passed'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    '''display python followed by param'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''display n is a number'''
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''displays a HTML page only if n is an integer'''
    return render_template('5-number.html', value=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

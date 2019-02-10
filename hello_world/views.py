from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request

MOJE_IMIE = "Pawel"
msg = "Witaj swiecie!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    imie = request.args.get('imie')
    return get_formatted(msg, MOJE_IMIE,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

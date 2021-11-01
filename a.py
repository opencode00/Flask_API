from flask import Flask
from PepaPig import pepapig_functions as ppfx

app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers['Access-Control-Allow-Methods'] = '*'
    r.headers['Access-Control-Allow-Headers'] = '*'
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

@app.route('/pepapig/primitiva')
def primitiva():
    data = ppfx.primitiva_numbers()
    return data

@app.route('/pepapig/euromillones')
def euromillones():
    data = ppfx.euromillones_numbers()
    return data

app.run(port=5001)

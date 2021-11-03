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
    return ppfx.primitiva_numbers()

@app.route('/pepapig/euromillones')
def euromillones():
    return ppfx.euromillones_numbers()

app.run(port=5001)

from flask import Flask
from flask_cors import CORS
from PepaPig import primitiva_get_numbers as prnum
from PepaPig import euromillones_get_numbers as eunum

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/pepapig/primitiva')
def primitiva():
    data = prnum.get_numbers()
    return data

@app.route('/pepapig/euromillones')
def euromillones():
    data = eunum.get_numbers()
    return data

app.run(port=5001)
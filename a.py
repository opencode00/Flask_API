from flask import Flask, request
# from PepaPig import pepapig_functions as ppfx
from Model import model_api as mapi

app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers['Access-Control-Allow-Methods'] = '*'
    r.headers['Access-Control-Allow-Headers'] = '*'
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

@app.route('/listman/add')
def add():
    #Querystring: request.args.get('par')
    return mapi.add()

#@app.route('/form-example', methods=['GET', 'POST'])
# if request.method == 'POST':
#     language = request.form.get('language')

# @app.route('/pepapig/primitiva')
# def primitiva():
#     return 'primitiva desde la api de python en el 5001'
#     # return ppfx.primitiva_numbers()

# @app.route('/pepapig/euromillones')
# def euromillones():
#     return 'euromillones desde la api de python en el 5001'
#     # return ppfx.euromillones_numbers()

app.run(port=5001)

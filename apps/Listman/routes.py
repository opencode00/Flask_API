import hashlib
from datetime import datetime
from apps.Model import model
from flask import Blueprint, request, jsonify, current_app as app

# Blueprint Configuration
listman_bp = Blueprint(
    'listman_bp', __name__,
)

def protect(token):
    key = app.config['KEY']+datetime.strftime(datetime.now(), "%H")
    md5 = hashlib.md5()
    md5.update(key.encode())
    print(md5.hexdigest())
    if token == md5.hexdigest():
        return True
    exit()

@listman_bp.route('/givemepower', methods=["POST"])
def givemepower():
    if (request.form.get('user') == app.config['USER'] and request.form.get('pass') == app.config['PASS']): 
        key = app.config['KEY']+datetime.strftime(datetime.now(), "%H")
        md5 = hashlib.md5()
        md5.update(key.encode())
        return md5.hexdigest()
    return ''

@listman_bp.route('/listman/add', methods=["POST"])
def listman_add(): #(tipo, name, value, name_data=None):
    #añade un valor nodo y dato
    protect(request.args.get('key'))
    data = dict(request.form)
    print(data)
    if 'name_data' not in data.keys():
        data['name_data'] = data['name']

    type = model.select("types", 'rowid', f"name like '{data['type']}'")[0][0]
    node_id = model.insert("nodes", name=data['name'], slug=model.slugify(data['name']), type=type, active=1)
    model.insert('data', id_node=node_id, name=data['name_data'], slug=model.slugify(data['name']), value=data['value'])

    return ''
    
@listman_bp.route('/listman/remove/<int:id>')
def listman_remove(id):
    #elimina un nodo y los datos asociados
    protect(request.args.get('key'))
    model.delete("nodes", id)
    model.delete("data", id, "id_node")
    return ''

@listman_bp.route('/listman/get/<string:type>')
def listman_get(type):
    #devuelve 
    # protect(request.args.get('key'))
    tipo = model.select("types", 'rowid', f"name like '{type}'")[0][0]
    node_id = model.select("nodes", "ROWID", f"type={tipo}")[0][0]
    data = model.get_full_data(f"A.type=1")
    return jsonify(data)
    

@listman_bp.after_request
def add_header(r):
    r.headers['Access-Control-Allow-Methods'] = '*'
    r.headers['Access-Control-Allow-Headers'] = '*'
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r
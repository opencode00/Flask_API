from flask import Flask, request
# from PepaPig import pepapig_functions as ppfx
app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers['Access-Control-Allow-Methods'] = '*'
    r.headers['Access-Control-Allow-Headers'] = '*'
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r

@app.route('/listman/add', methods=["POST"])
def add(): #(tipo, name, value, name_data=None):
    #añade un valor nodo y dato
    from Model import model
    data = dict(request.form)
    if 'name_data' not in data.keys():
        data['name_data'] = data['name']

    type = model.select("types  ", 'rowid', f"name like '{data['type']}'")[0][0]
    node_id = model.insert("nodes", name=data['name'], slug=model.slugify(data['name']), type=type, active=1)
    model.insert('data', id_node=node_id, name=data['name_data'], slug=model.slugify(data['name']), value=data['value'])

    return ''

@app.route('/listman/remove/<int:id>')
def remove(id):
    #elimina un nodo y los datos asociados
    from Model import model
    model.delete("nodes", id)
    model.delete("data", id, "id_node")
    return ''

app.run(port=5001)
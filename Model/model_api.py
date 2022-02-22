import model

def add (tipo, name, value, name_data=None):
    #añade un valor nodo y dato
    if name_data is None:
        name_data = name
    type = model.select("types", 'rowid', f"name like '{tipo}'")[0][0]
    node_id = model.insert("nodes", name=name, slug=model.slugify(name), type=type, active=1)
    model.insert('data', id_node=node_id, name=name_data, slug=model.slugify(name), value=value)

def remove (id_nodo):
    model.delete("nodes", id_nodo)
    model.delete("data", id_nodo, 'id_node')

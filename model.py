import sqlite3

conn = sqlite3.connect('serebro.db')
c = conn.cursor()
tables={
    'nodes': {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT', # Valor para mostrar
        'slug': 'TEXT', # Valor para request
        'type': 'INTEGER',
        'active': 'INTEGER',
        'allowed': 'TEXT'
    },
    'data':{
        'id': 'INTEGER PRIMARY KEY',
        'id_node': 'INTEGER',
        'name': 'TEXT',
        'slug': 'TEXT',
        'value': 'TEXT'
    },
    'types': {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT',
        'icono': 'TEXT'
    }
}
for table,value in tables.items():
    query=""
    pairs = list(zip(value.keys(),value.values()))
    for p in pairs:
        query = query + f'{p[0]} {p[1]},'
    # print(f"CREATE TABLE IF NOT EXISTS {table} ({query[:-1]});")
    c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({query[:-1]});")
   
def get_nodes():
    c.execute(f"SELECT rowid, {','.join(tables['nodes'].keys())} FROM nodes")
    return c.fetchall()

def get_data(node):
    c.execute(f"SELECT rowid, {','.join(tables['data'].keys())} FROM FROM data WHERE id_nodo = :id_nodo", {'id_nodo':node})
    return c.fetchall()

def get_types():
    c.execute(f"SELECT rowid, {','.join(tables['data'].keys())} FROM types")
    return c.fetchall()

def add_type(name):
    with conn:
        return c.execute('INSERT INTO types VALUES (NULL, :name)',{'name': name})

def add_node(name, type, active=1, allowed=None):
    with conn:
        return c.execute('INSERT INTO nodos VALUES (NULL, :name, :slug, :type, :active, :allowed)',{'name':name, 'slug': slugify(name), 'type': type, 'active':active, 'allowed':allowed}).lastrowid
  
def add_data(nodo, name, value):
    with conn:
        c.execute('INSERT INTO nodos_datos VALUES (NULL, :id_nodo, :name, :slug, :value)',
        {'id_nodo':nodo, 'name': name, 'slug':slugify(name), 'value': value })

def update_node(id, **args):
    """
    update_node(id, **args):
    :id id del nodo 
    :**args (name, type, active, allowed)
    """
    # print(args.items())
    campos=[]
    values=[]
    for key,value in args.items():
        if value != "" or value is None:
            if(key == 'name'):
                campos.append("slug=?")
                values.append(slugify(value))
            if(key == "slug"):
                continue
            values.append(value)
            campos.append(key+"=?")
    query = f'UPDATE nodos SET {",".join(campos)} WHERE id={id}'
    # print(query)
    # print(values)
    with conn:
        c.execute(query, values)

def update_data(id, name, value=None):
    """
    update_node(id, name, value):
    :id id 
    :name
    :value
    """
    if(value is None):
        query = f'UPDATE nodos_datos SET name="{name}", slug="{slugify(name)}" WHERE id={int(id)}'
    else:
        query = f'UPDATE nodos_datos SET name="{name}", value="{value}", slug="{slugify(name)}" WHERE id={int(id)}'
    with conn:
        c.execute(query)

def update_types():
    query = f'UPDATE types SET name="{name}", value="{value}", slug="{slugify(name)}" WHERE id={int(id)}'
    with conn:
        c.execute(query)



def slugify(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace('á','a')
    cadena = cadena.replace('é','e')
    cadena = cadena.replace('í','i')
    cadena = cadena.replace('ó','o')
    cadena = cadena.replace('ú','u')
    cadena = cadena.replace('ñ','n')
    cadena = cadena.replace(' ','_')
    return cadena
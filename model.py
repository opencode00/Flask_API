import sqlite3

conn = sqlite3.connect('serebro.db')
c = conn.cursor()
tables={
    'nodes': {
        # 'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT', # Valor para mostrar
        'slug': 'TEXT', # Valor para request
        'type': 'INTEGER',
        'active': 'INTEGER'
    },
    'data':{
        # 'id': 'INTEGER PRIMARY KEY',
        'id_node': 'INTEGER',
        'name': 'TEXT',
        'slug': 'TEXT',
        'value': 'TEXT'
    },
    'types': {
        # 'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT'
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
    c.execute(f"SELECT rowid, {','.join(tables['data'].keys())} FROM data WHERE id_node = :id_nodo", {'id_nodo':node})
    return c.fetchall()

def get_types():
    c.execute(f"SELECT rowid, {','.join(tables['types'].keys())} FROM types")
    return c.fetchall()

def get_full_data(node):
    c.execute(f"SELECT A.ROWID,A.*,B.ROWID, B.* FROM nodes A INNER JOIN data B ON A.ROWID = B.id_node WHERE A.ROWID = :id_nodo", {'id_nodo':node})
    return c.fetchall()

def add_type(**args):
    """
    add_type(**args)
        name => nombre del tipo
    """
    fields = []
    values = []
    for field in tables['types'].keys():
        if field == 'id':
            continue
        fields.append(':'+field)
        values.append(args.get(field))
    print(f"INSERT INTO types VALUES ({','.join(fields)})  -> {values}")
    with conn:
        return c.execute(f"INSERT INTO types VALUES ({','.join(fields)})",values)

def add_node(**args):
    """
    add_node(**args)
        name => nombre del nodo
        slug => nombre simplificado para acceder via URL
        type  => tipo de dato (indice tabla type)
        active => nodo activo
    """
    fields = []
    values = []
    for field in tables['nodes'].keys():
        if field == 'id':
            continue
        values.append(args.get(field))
        fields.append(':'+field)
    print(f"INSERT INTO nodes VALUES ({','.join(fields)})  -> {values}")
    with conn:
        return c.execute(f"INSERT INTO nodes VALUES ({','.join(fields)})",values).lastrowid
  
def add_data(**args):
    """
    add_data(**args)
        id_node => id del nodo para agrupar
        name => nombre del dato para impresion
        slug => nombre simplificado para acceso via URL
        value  => valor del dato.
    """
    fields = []
    values = []
    for field in tables['data'].keys():
        values.append(args.get(field))
        fields.append(':'+field)
    print(f"INSERT INTO data VALUES ({','.join(fields)})  -> {values}")    
 
    with conn:
        c.execute(f"INSERT INTO data VALUES ({','.join(fields)})",values).lastrowid

def update_node(id, **args):
    """
    update_node(id, **args):
        id => id del nodo 
        name
        type
        active
    """
    fields=[]
    values=[]
    for field in tables['nodes'].keys():
        values.append(args.get(field))
        fields.append(field+'=?')
    query = f'UPDATE nodes SET ({",".join(fields)}) WHERE ROWID={id}'
    print(f"{query} => {values}")
    with conn:
        c.execute(query, values)

def update_data(id, **args):
    """
    update_node(**args):
        id  
        name
        value
    """
    if(value is None):
        query = f'UPDATE data SET name="{name}", slug="{slugify(name)}" WHERE id={int(id)}'
    else:
        query = f'UPDATE data SET name="{name}", value="{value}", slug="{slugify(name)}" WHERE id={int(id)}'
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


# def update_node(id, **args):
#     """
#     update_node(id, **args):
#         id => id del nodo 
#         name
#         type
#         active
#         allowed
#     """
#     # print(args.items())
#     campos=[]
#     values=[]
#     for key,value in args.items():
#         if value != "" or value is None:
#             if(key == 'name'):
#                 campos.append("slug=?")
#                 values.append(slugify(value))
#             if(key == "slug"):
#                 continue
#             values.append(value)
#             campos.append(key+"=?")
#     query = f'UPDATE nodes SET {",".join(campos)} WHERE ROWID={id}'
#     with conn:
#         c.execute(query, values)
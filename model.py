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

def insert(table, **args):
    """
    insert(table, **args)
        table => nombre de la tabla
        **args => campos de la tabla
    """
    fields = []
    values = []
    for field in tables[table].keys():
        values.append(args.get(field))
        fields.append(':'+field)
    print(f"INSERT INTO {table} VALUES ({','.join(fields)})  -> {values}")    
    with conn:
        c.execute(f"INSERT INTO {table} VALUES ({','.join(fields)})",values).lastrowid

def update(table, id, **args):
    """
    update(table, id, **args):
        table => nombre de la tabla a actualizar
        id => id del nodo 
        **args => campos de la tabla 
    """
    fields=[]
    values=[]
    for field in tables[table].keys():
        if args.get(field) is not None:
            values.append(args.get(field))
            fields.append(field+'=?')
    query = f'UPDATE {table} SET {",".join(fields)} WHERE ROWID={id}'
    # print(f"{query} => {values}")
    with conn:
        c.execute(query, values)

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
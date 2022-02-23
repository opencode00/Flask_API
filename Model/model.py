from pickle import FALSE
import sqlite3

conn = sqlite3.connect('serebro.db', check_same_thread=False)  ##Se va aa crear en el directorio de trabajo cwd, donde el primer script.
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
    with conn:
        c.execute(f"CREATE TABLE IF NOT EXISTS {table} ({query[:-1]});")
   
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

def select(table, select=None, where="1=1"):
    if select is None:
        select = f"rowid, {','.join(tables[table].keys())}"
    
    print(f"SELECT {select} FROM {table} WHERE {where}")
    with conn:
        c.execute(f"SELECT {select} FROM {table} WHERE {where}")
        return c.fetchall()

def insert(table, **args):
    """
    insert(table, **args)\n
        \ttable => nombre de la tabla\n
        \t**args => campos de la tabla\n
    """
    fields = []
    values = []
    for field in tables[table].keys():
        values.append(args.get(field))
        fields.append(':'+field)
    print(f"INSERT INTO {table} VALUES ({','.join(fields)})  -> {values}")    
    with conn:
        return c.execute(f"INSERT INTO {table} VALUES ({','.join(fields)})",values).lastrowid

def update(table, id, **args):
    """
    update(table, id, **args):\n
        \ttable => nombre de la tabla a actualizar\n
        \tid => id del nodo\n
        **args => campos de la tabla\n
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

def delete(table, id, field = "ROWID"):
    """
    delete(table, id):\n
        \ttable => nombre de la tabla a eliminar\n
        \tid => id del nodo 
    """
    query = f'DELETE FROM {table} WHERE {field}={id}'
    with conn:
        c.execute(query)

def get_full_data(where="1=1"):
    """
    A = nodes ; B= data ; C = types
    """
    with conn:
        query = f"""SELECT A.ROWID,A.name,C.name,A.active,B.rowid,B.name,B.value 
                    FROM nodes A 
                    INNER JOIN data B 
                    ON A.ROWID = B.id_node 
                    INNER JOIN types C
                    ON A.type = C.rowid
                    WHERE {where}"""
        c.execute(query)
        return c.fetchall()
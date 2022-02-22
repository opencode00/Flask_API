# TODO 
- API para model (preparado para usar con fetch con una sola llamada)
    - add (name, tipo, value, name_data=None) : añade un valor nodo y dato
    - getData(id, name, value) : obtiene el registro completo del dato que conincida con id, nombre o valor
    - remove (id_nodo) : elimina el nodo y sus datos asociados 
    - 



## Proceso de inicializacion y comprobación del modelo
py -i testModel.py #al instanciar model ya se crea las tablas y su estructura.
init() # esta parte inserta datos de prueba
show_nodes()
update_nodes()
show_nodes()
show_data(1)
show_data(2)
update_data()
show_data(1)
show_data(2)
show_types()
update_types()
show_types()

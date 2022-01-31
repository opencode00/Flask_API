import model

def init():
    init_types()
    init_nodes()
    init_data()

def show_nodes(node=False):
    print(model.get_nodes())

def show_data(node=False):
    print(model.get_data(node))

def show_types():
    print(model.get_types())

def show_full_data(node):
    print(model.get_full_data(node))

def init_types():
    model.add_type(name='Favoritos')

def init_nodes():
    model.add_node(name='Curso Python', type=1, active=1)
    model.add_node(name='Curso Node', type=1, active=1)

def init_data():
    model.add_data(id_node=1, name='Arrays', slug="arrays", value='D:\\work\\python\\lists.pdf')
    model.add_data(id_node=1, name='Objetos',slug="objetos", value='D:\\work\\python\\obj.pdf')
    model.add_data(id_node=2, name='Arrays', slug="arrays", value='D:\\work\\nodeJS\\lists.pdf')
    model.add_data(id_node=2, name='Objetos',slug="objetos", value='D:\\work\\nodeJS\\obj.pdf')

def update_node():
    model.update_node(1, name="Curso Python3", type=1, active=0)
    model.update_node(2, name="Curso NodeJS", type=1, active=0)

def update_data():
    model.update_data(1, "Lists")
    model.update_data(4,"ObjetosJS","D:\work\\nodeJS\\nodeObj.pdf")
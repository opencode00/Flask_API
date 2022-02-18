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
    model.insert("types", name='Favs')

def init_nodes():
    model.insert("nodes", name='Curso Python', type=0, active=1)
    model.insert("nodes", name='Curso Node', type=0, active=1)

def init_data():
    model.insert("data", id_node=1, name='Arrays', slug="arrays", value='D:\\work\\python\\lists.pdf')
    model.insert("data", id_node=1, name='Objetos',slug="objetos", value='D:\\work\\python\\obj.pdf')
    model.insert("data", id_node=2, name='Arrays', slug="arrays", value='D:\\work\\nodeJS\\lists.pdf')
    model.insert("data", id_node=2, name='Objetos',slug="objetos", value='D:\\work\\nodeJS\\obj.pdf')


def update_nodes():
    model.update("nodes", 1, name="Curso Python3")
    model.update("nodes", 2, name="Curso NodeJS", type=1, active=0)

def update_data():
    model.update("data", 1, name="Lists")
    model.update("data", 4, name="ObjetosJS",value="D:\work\\nodeJS\\nodeObj.pdf")

def update_types():
    model.update("types", 1, name="Favorites")
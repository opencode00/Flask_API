import model

def init_data():
    model.add_type('Favoritos')
    model.add_node('Curso Python', 1)
    model.add_data(1, 'Arrays', 'D:\\work\\python\\lists.pdf')
    model.add_data(1, 'Objetos', 'D:\\work\\python\\obj.pdf')
    model.add_node('Curso Node', 1)
    model.add_data(2, 'Arrays', 'D:\\work\\nodeJS\\lists.pdf')
    model.add_data(2, 'Objetos', 'D:\\work\\nodeJS\\obj.pdf')

def show_data(node=False):
    print(model.get_types())
    print(model.get_nodes())
    print(model.get_data(node))

def update_node():
    model.update_node(1, name="Curso Python3", type=1, active=0, allowed="Admins")
    model.update_node(2, name="Curso NodeJS", type=1, active=0, allowed="Users")


def update_data():
    model.update_data(1, "Lists")
    model.update_data(4,"ObjetosJS","D:\work\\nodeJS\\nodeObj.pdf")


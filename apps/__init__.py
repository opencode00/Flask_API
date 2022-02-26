"""Initialize Flask app."""
from flask import Flask


#aqui inicializaríamos el plugin de ser necesario.

def init_app():
    """
    Inicializamos Flask y cargamos todo lo que queramos que tenga la app. 
    Lo que no este aqui -NO EXISTE
    """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Logica y modulos de nuestra app
        from apps.Listman import routes as listman
        from apps.Drive import routes as drive

        # Register Blueprints
        app.register_blueprint(listman.listman_bp)
        app.register_blueprint(drive.drive_bp)

        return app
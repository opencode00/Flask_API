from flask import Blueprint, request, current_app as app

# Blueprint Configuration
drive_bp = Blueprint(
    'drive_bp', __name__,
)

@drive_bp.route('/drive/list')
def list():
    path = request.args.get('path') or None
    if (path is None or path <= app.config['INIT_DIR']):
        path = app.config['INIT_DIR']

    print(path)
    return path
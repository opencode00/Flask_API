from flask import Blueprint, request, json, send_file, current_app as app
from werkzeug.utils import secure_filename
import apps.Drive.drive as drive

# Blueprint Configuration
drive_bp = Blueprint(
    'drive_bp', __name__,
)

@drive_bp.route('/drive/list')
def list():
    path = request.args.get('path') or None
    if (path is None or len(path) <= len(app.config['INIT_DIR'])):
        path = app.config['INIT_DIR']
    
    return json.jsonify(drive.getFiles(path))

@drive_bp.route('/drive/viewfile')
def viewfile():
    path = request.args.get('path')
    if app.config['INIT_DIR'].replace(app.config['DIR_SEP'], app.config['DIR_SEP']*2) in path:
        return send_file(path)
    exit()

#?path=<directorio actual>&dir=<nombre del directorio>
@drive_bp.route('/drive/mkdir')
def mkdir():
    path = request.args.get('path')
    dir = request.args.get('dir')
    drive.mkdir(path+app.config['DIR_SEP']+dir)
    return ''

#?opath=<path de origen>&dpath=<path de destino>
@drive_bp.route('/drive/mv')
def mv():
    src = request.args.get('opath')
    dst = request.args.get('dpath')
    drive.mv(src,dst)
    return ''

#?opath=<path de origen>&dpath=<path de destino>
@drive_bp.route('/drive/cp')
def cp():
    src = request.args.get('opath')
    dst = request.args.get('dpath')
    drive.cp(src,dst)
    return ''

# path=<ruta relativa>&uploadFile=<fichero a subir>
@drive_bp.route("/drive/upload", methods=['POST'])
def uploader():
    path = request.form.get('path')
    files = request.files.getlist('uploadFile')
    for file in files:
        filename = secure_filename(file.filename)
        file.save(path, filename)
    return ""
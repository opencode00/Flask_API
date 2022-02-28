from flask import Blueprint, make_response, request, json, send_file, current_app as app
from werkzeug.utils import secure_filename
import apps.Drive.drive as drive
import os
import apps.common as utils

# Blueprint Configuration
drive_bp = Blueprint(
    'drive_bp', __name__,
)

@drive_bp.before_app_request
def protect():
    if request.args.get('key') != utils.gen_key():
        make_response("Error", 403)
    
@drive_bp.route('/drive/list')
def list():
    path = request.args.get('path') or None
    if (path is None or len(path) <= len(app.config['INIT_DIR'])):
        path = app.config['INIT_DIR']
    
    return json.jsonify(drive.getFiles(path))

@drive_bp.route('/drive/viewFile')
def viewfile():
    path = request.args.get('path')
    if os.path.exists(path):
        return send_file(path)
    return ''

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
@drive_bp.route("/drive/upload", methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        path = request.form.get('path')
        print('POST')
        print(path)
        files = request.files.getlist('uploadFile')
        print(files)
        for file in files:
            print(file)
            filename = secure_filename(file.filename)
            file.save(path, filename)

    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" enctype="multipart/form-data">
        <input type=file name=uploadFile>
        <input type=hidden name=path value="d:\\pedro\\test\\prueba6">
        <input type="submit">
    </form>
</body>
</html>
    """

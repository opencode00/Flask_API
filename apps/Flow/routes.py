from flask import Blueprint, make_response, request, json, send_file, current_app as app
import apps.common as utils
import os
from apps.Drive.drive import getMimeTypes

# Blueprint Configuration
flow_bp = Blueprint(
    'flow_bp', __name__,
)

@flow_bp.route('/view')
def view():
    path = request.args.get('path')
    if os.path.exists(path):
        mime = getMimeTypes(path)[0]
        return utils.streamFile(path, mime)

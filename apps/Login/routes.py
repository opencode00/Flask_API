from ctypes import util
from flask import Blueprint, make_response, request, jsonify, current_app as app
import apps.common as utils

# Blueprint Configuration
login_bp = Blueprint(
    'login_bp', __name__,
)

@login_bp.route('/givemepower', methods=["POST"])
def givemepower():
    if (request.form.get('user') == app.config['USER'] and request.form.get('pass') == app.config['PASS']): 
        utils.gen_key()
    return ''


@login_bp.route('/login', methods=['POST'])
def login():
    if request.form.get('user') == app.config['USER'] and request.form.get('pass') == app.config['PASS']:
        return utils.gen_key()
    else:
        return make_response("Error", 403)
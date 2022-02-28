# funcionalidades comunes
import hashlib
from datetime import datetime
from flask import current_app as app

def gen_key():
    key = app.config['SECRET_KEY']+datetime.strftime(datetime.now(), "%H")
    md5 = hashlib.md5()
    md5.update(key.encode())
    return md5.hexdigest()

def protect(token):
    if token == gen_key():
        return True
    exit()
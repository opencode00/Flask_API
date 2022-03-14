# funcionalidades comunes
import hashlib
import re
from os import path
from datetime import datetime
from apps.Drive.drive import getFileSize
from flask import request, Response, current_app as app

### Protect ####
def gen_key():
    key = app.config['SECRET_KEY']+datetime.strftime(datetime.now(), "%H")
    md5 = hashlib.md5()
    md5.update(key.encode())
    return md5.hexdigest()

def protect(token):
    if token == gen_key():
        return True
    exit()
##############

def streamFile(file, mime):
    range = request.headers.get('Range', None)
    start,end=0,(1024**2)
    if range:
        start, end = range.replace("bytes=", "").split("-")
        start = int(start)
        end = int(start + (1024**2))

    # LEEMOS LA POSICION EXACTA DEL ARCHIVO

    with open(file, "rb") as myfile:
        myfile.seek(start)
        data = myfile.read(end - start)
        size_video = str(path.getsize(file))

        resp = Response(data, 206, mimetype=mime, content_type=mime, direct_passthrough=True)
        resp.headers.add ('Content-Range', f'bytes {str(start)}-{str(end)}/{size_video}')
        resp.headers.add ('Accept-Ranges', 'bytes')
        return resp


### Streaming ####
# def streamFile(path, mime):
#     range_header = request.headers.get('Range', None)
#     byte1, byte2 = 0, None
#     if range_header:
#         match = re.search(r'(\d+)-(\d*)', range_header)
#         groups = match.groups()
#         if groups[0]:
#             byte1 = int(groups[0])
#         if groups[1]:
#             byte2 = int(groups[1])
#     chunk, start, length, file_size = get_chunk(path, byte1, byte2)
#     resp = Response(chunk, 206, mimetype=mime,
#                     content_type=mime, direct_passthrough=True)
#     resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
#     return resp

# def get_chunk(path, byte1=0, byte2=0):
#     size = getFileSize(path)
#     start = 0
#     if byte1 < size:
#         start = byte1
#     if byte2:
#         length = byte2 + 1 - byte1
#     else:
#         length = size-start
    
#     with open (path, "rb") as f:
#         f.seek(start)
#         chunk = f.read(length)
#     return chunk, start, length, size

    ##############
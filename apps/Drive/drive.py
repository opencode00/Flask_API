import os
import shutil
import math
import mimetypes

def getFiles(path):
    tree =[]
    dirs=[]
    files=[]
    if os.path.exists(path):
        with os.scandir(path) as entries:
            for entry in sorted(entries, key=lambda x: x.name):
                el = {}
                if entry.is_dir():
                    el['name'] = entry.name
                    el['location'] = entry.path
                    dirs.append(el)
               
                if entry.is_file():
                    el['name'] = entry.name
                    el['location'] = entry.path
                    el['size'] = humanSize(entry.stat().st_size)
                    files.append(el)

    tree.append(path)
    tree.append(dirs)
    tree.append(files)
    return tree

def getFileSize(path):
    return os.stat(path).st_size

#no se usa en web
def getMimeTypes(path):
    return mimetypes.guess_type(path)

#no se usa en web
def viewFileContent(path):
    if os.path.exists(path) and os.path.isfile(path):
        with open (path, 'rb') as f:
            return f.read()

def mkdir(path):
    try:
        os.mkdir(path)
    except:
        pass

#no se usa en web
def rm (path):
    try:
        os.remove(path)
    except:
        pass

def mv (src, dst):
    try:
        if (os.path.isdir(dst)):
            shutil.move(src,dst)
        else:
            os.rename(src, dst)
    except:
        pass

def cp (src, dst):
    try:
        if (os.path.isdir(src)):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    except:
        pass


def humanSize(size):
    sz = 'BKMGTP'
    lg = len(str(size))
    factor = math.floor((lg-1)/3)
    tam = round(size/(1024**factor),2)
    return f"{tam} {sz[int(factor)]}"

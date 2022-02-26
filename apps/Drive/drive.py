import os
import math
import mimetypes

def getFiles(path):
    dirs=[]
    files=[]
    if os.path.exists(path):
        with os.scandir(path) as entries:
            for entry in entries:
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

    return [path]+[*dirs]+[*files]

def getMimeTypes(path):
    return mimetypes.guess_type(path)

def viewFile(path):
    if os.path.exists(path) and os.path.isfile(path):
        with open (path, 'rb') as f:
            return f.read()

def mkdir(path):
    try:
        os.mkdir(path)
    except:
        pass


# function rm(path){
# function mv(oPath,dPath){
# function cp(oPath,dPath){
# function upload(oPath,file){
def humanSize(size):
    sz = 'BKMGTP'
    lg = len(str(size))
    factor = math.floor((lg-1)/3)
    tam = round(size/(1024**factor),2)
    return f"{tam} {sz[int(factor)]}"

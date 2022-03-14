import os
from apps.Drive.routes import get_chunk, viewfile as view

## Reproductor WEB
## reproducir todas las pistas
## reproducir todas la pistas de un directorio
## reproducir una canción
## añadir una cancion a la cola de reproduccion
## añadir un directorio a la cola de reproduccion
## buscar canciones
## 
## API (http://www.subsonic.org/pages/api.jsp)(https://www.navidrome.org/docs/developers/subsonic-api/)
## reproducir todas las pistas
## reproducir todas la pistas de un directorio
## reproducir una canción
## añadir una cancion a la cola de reproduccion
## añadir un directorio a la cola de reproduccion
## buscar canciones


test = 'd:/pedro/test/selections'
def getFolders(path):
    return [(dirs.path, dirs.name) for dirs in os.scandir(path) if dirs.is_dir()]

def getFolderSongs(path):
    return [(files.path, files.name) for files in os.scandir(path) if files.is_file()]

def getAllSongs(path):
    songs = []
    for dir, dirs, files in os.walk(path):
        for file in files:
            songs.append((dir,file)) 
            
    return songs


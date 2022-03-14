"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    #----Mias 
    SECRET_KEY = environ.get('KEY')
    USER = environ.get('APP_USER')
    PASS = environ.get('APP_PASS')
    INIT_DIR = environ.get('INIT_DIR')
    DIR_SEP = environ.get('DIR_SEP')
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
init =os.path.dirname(os.path.abspath(__name__)) 
from f"os.path.dirname(os.path.abspath(__name__))/config" import Config

# file = os.path.dirname(os.path.abspath(__name__))+'//config//pepapigcred.json'
file = '/work/www/APY/apps/Peppapig/config/pepapigcred.json'

def get_client():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(file, scope)
    return gspread.authorize(creds)

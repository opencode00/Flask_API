import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_client():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("d:/APY/PepaPig/config/pepapigcred.json", scope)
    return gspread.authorize(creds)
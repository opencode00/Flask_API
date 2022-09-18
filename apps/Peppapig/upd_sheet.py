from gsheets_creds import get_client
import common

client = get_client()

def euro_sheet(combinacion):
    sheet = client.open("Euromillones").sheet1  # Open the spreadhseet
    for c in combinacion:
        common.euro_sheet(sheet, c)

def primi_sheet(combinacion):
    sheet = client.open("Primitiva").sheet1  # Open the spreadhseet
    for c in combinacion:
        common.primi_sheet(sheet, c)

def bono_sheet(combinacion):
    sheet = client.open("Bonoloto").sheet1  # Open the spreadhseet
    for c in combinacion:
        common.bono_sheet(sheet, c)
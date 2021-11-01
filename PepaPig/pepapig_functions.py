from .gsheets_creds import get_client
import json

def euromillones_process_column(col):
    data=[]
    data.append(col[1])
    data.append(col[2])
    data.append(col[3])
    data.append(col[4])
    data.append(col[5])
    data.append(col[6])
    data.append(col[7])
    data.append(col[8])
    data.append(col[15])
    return data

def euromillones_stars(row):
    return f'Top Stars: {row[1]}, {row[2]}'

def euromillones_numbers():
    client = get_client()
    file = client.open("Euromillones")
    sheet = file.get_worksheet(2)
    data = []
    data.append(euromillones_process_column(sheet.col_values(2)))
    data.append(euromillones_process_column(sheet.col_values(3)))
    data.append(euromillones_process_column(sheet.col_values(4)))
    data.append(euromillones_process_column(sheet.col_values(5)))
    data.append(euromillones_process_column(sheet.col_values(6)))
    data.append(euromillones_process_column(sheet.col_values(7)))
    data.append(euromillones_stars(sheet.row_values(18)))
    # with open('data\\euromillones_combinacion.json','w') as file:
    return json.dumps(data)

def primitiva_process_column(col):
    data=[]
    data.append(col[0])
    data.append(col[1])
    data.append(col[2])
    data.append(col[3])
    data.append(col[4])
    data.append(col[5])
    data.append(col[6])
    data.append(col[7])
    data.append(col[16])
    return data

def primitiva_numbers():
    client = get_client()
    file = client.open("Primitiva")
    sheet = file.get_worksheet(2)
    data = []
    data.append(primitiva_process_column(sheet.col_values(2)))
    data.append(primitiva_process_column(sheet.col_values(3)))
    data.append(primitiva_process_column(sheet.col_values(4)))
    data.append(primitiva_process_column(sheet.col_values(5)))
    data.append(primitiva_process_column(sheet.col_values(6)))
    data.append(primitiva_process_column(sheet.col_values(7)))
    # with open('data\\primitiva_combinacion.json','w') as file:
    return json.dumps(data)


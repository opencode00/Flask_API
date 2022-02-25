from .gsheets_creds import get_client
import json

def process_column(col):
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

def get_top_stars(row):
    return f'Top Stars: {row[1]}, {row[2]}'
    
def get_numbers():
    client = get_client()
    file = client.open("Euromillones")
    sheet = file.get_worksheet(2)
    data = []
    data.append(process_column(sheet.col_values(2)))
    data.append(process_column(sheet.col_values(3)))
    data.append(process_column(sheet.col_values(4)))
    data.append(process_column(sheet.col_values(5)))
    data.append(process_column(sheet.col_values(6)))
    data.append(process_column(sheet.col_values(7)))
    data.append(get_top_stars(sheet.row_values(18)))
    # with open('data\\euromillones_combinacion.json','w') as file:
    #     json.dump(data, file)
    return json.dumps(data)
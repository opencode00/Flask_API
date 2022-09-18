from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}


def euro_process(item):
    fecha = str(item['fecha_sorteo'])[0:10]
    dia = datetime.strptime(fecha,"%Y-%m-%d").weekday()
    
    combinacion = str(item['combinacion_acta']).replace('-',',')
    if combinacion is None:
        combinacion = str(item['combinacion']).replace('-',',')
    
    return f"{fecha},{dia},{combinacion}".replace(" ","")


def primi_process(item):
    fecha = str(item['fecha_sorteo'])[0:10]
    dia = datetime.strptime(fecha,"%Y-%m-%d").weekday()

    combinacion = str(item['combinacion_acta']).replace('-',',')
    if combinacion is None or combinacion == 'None':
        combinacion = str(item['combinacion']).replace('-',',')
    
    combinacion = str(combinacion).replace('(','')
    combinacion = combinacion.replace(')','')
    combinacion = combinacion.replace('C','-')
    combinacion = combinacion.replace('R','-')
    combinacion = combinacion.replace('-',',')
    
    return f"{fecha},{dia},{combinacion}".replace(" ","")

def bono_process(item):
    return primi_process(item)

def euro_sheet(sheet, comb):
    if (comb):
        last_date = sheet.get_values(f'A{sheet.row_count}')[0][0]
        combinacion = comb.split(',')
        if last_date != combinacion[0]:
            sheet.append_row(combinacion, 'USER_ENTERED', 'INSERT_ROWS', 'A:I')

def primi_sheet(sheet, comb):
    if (comb):
        last_date = sheet.get_values(f'A{sheet.row_count}')[0][0]
        combinacion = comb.split(',')
        if last_date != combinacion[0]:
            sheet.append_row(combinacion, 'USER_ENTERED', 'INSERT_ROWS','A:N')

def bono_sheet(sheet, comb):
    if (comb):
        last_date = sheet.get_values(f'A{sheet.row_count}')[0][0]
        combinacion = comb.split(',')
        if last_date != combinacion[0]:
            sheet.append_row(combinacion, 'USER_ENTERED', 'INSERT_ROWS','A:N')


def writeCSV(file, line):
    with open(f'{file}_hist.csv', 'a') as sheet:
        sheet.write(line)
        sheet.write('\n')


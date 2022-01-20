import requests as rq
import json
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}


def make_sheet(data):
    with open('primitiva_sheets.csv', 'a') as sheet:
        for item in data:
            fecha = str(item['fecha_sorteo'])[0:10]
            #fecha = datetime.strptime(fecha,'%Y-%m-%d')
            fecha = datetime.strftime(fecha, '%d/%m/%Y')
            dia = 4
            if item['dia_semana'] != 'jueves':
                dia = 6
            combinacion = str(item['combinacion']).replace('(','')
            combinacion = combinacion.replace(')','')
            combinacion = combinacion.replace('C','-')
            combinacion = combinacion.replace('R','-')
            combinacion = combinacion.replace('-',',')


            cadena = f"{fecha}, {dia}, {combinacion}"
            # print (cadena.replace(' ',''))
            sheet.write(cadena.replace(' ',''))
            sheet.write('\n')


with open('primitiva_raw.json', 'a') as primi:
    web = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=LAPR&celebrados=true&fechaInicioInclusiva=19850101&fechaFinInclusiva=19851231'
    response = rq.get(web, headers=headers)
    data_raw = response.json()
    json.dump(data_raw, primi)
    make_sheet(data_raw)
    
    for year in range(1986, 2022):
        web1 = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=LAPR&celebrados=true&fechaInicioInclusiva={year}0101&fechaFinInclusiva={year}0630'
        response1 = rq.get(web1, headers=headers)
        web2 = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=LAPR&celebrados=true&fechaInicioInclusiva={year}0701&fechaFinInclusiva={year}1231'
        response2 = rq.get(web2, headers=headers)
        
        semestre1 = response1.json()
        semestre2 = response2.json()
        semestre1.extend(semestre2)
        json.dump(semestre1, primi)
        make_sheet(semestre1)





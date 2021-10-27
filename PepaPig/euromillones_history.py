import requests as rq
import json
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}

with open('euromillones_raw.json', 'a') as euro:
    for year in range(2004, 2022):
        web1 = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=EMIL&celebrados=true&fechaInicioInclusiva={year}0101&fechaFinInclusiva={year}0630'
        web2 = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=EMIL&celebrados=true&fechaInicioInclusiva={year}0701&fechaFinInclusiva={year}1231'
        response1 = rq.get(web1, headers=headers)
        response2 = rq.get(web2, headers=headers)
        data_raw = response1.json()
        semestre2 = response2.json()
        data_raw.extend(semestre2)
        json.dump(data_raw, euro)

        with open('euromillones_sheets.csv', 'a') as sheet:
            for item in data_raw:
                fecha = str(item['fecha_sorteo'])[0:10]
                fecha = datetime.strftime(fecha, '%d/%m/%Y')
                dia = 5
                if item['dia_semana'] != 'viernes':
                    dia = 2
                combinacion = str(item['combinacion']).replace('-',',')

                cadena = f"{fecha}, {dia}, {combinacion}"
                # print (cadena.replace(' ',''))
                sheet.write(cadena.replace(' ',''))
                sheet.write('\n')

import requests as rq
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}

def euromillones_ayer():
    now = datetime.now()
    # today= f'20211015'
    today= f'{now.year}{now.month}{now.day-1}'
    web = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=EMIL&celebrados=true&fechaInicioInclusiva={today}&fechaFinInclusiva={today}'
    response = rq.get(web, headers=headers)
    data_raw = response.json()
    if (isinstance(data_raw, list)):
        dato = []
        # fecha = datetime.strftime(now, '%d/%m/%Y')
        dato.append(f'{now.day-1}/{now.month}/{now.year}')
        dia = 5
        if data_raw[0]['dia_semana'] != 'viernes':
            dia = 2
        dato.append(dia)
        combinacion = str(data_raw[0]['combinacion']).replace('-',',')
        combinacion = combinacion.replace(' ','')
        # print(data_raw)
        combinacion = combinacion.split(',')
        for columna in combinacion:
            dato.append(columna)
    
        return dato
    return False

import requests as rq
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'
           'q=0.9,image/webp,*/*;q=0.8'}

def primitiva_ayer():
    now = datetime.now()
    today= f'{now.year}{now.month}{now.day-1}'
    # today='20211016'
    
    web = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id=LAPR&celebrados=true&fechaInicioInclusiva={today}&fechaFinInclusiva={today}'
    response = rq.get(web, headers=headers)
   
    if (response.status_code == 200):
        data_raw = response.json()
        # print(data_raw)
        dato = []
        dato.append(f'{now.day-1}/{now.month}/{now.year}')
        if (data_raw[0]['dia_semana'] == 'jueves'):
            dato.append(4)
        else:
            dato.append(6)
        combinacion = str(data_raw[0]['combinacion']).replace('(','')
        combinacion = combinacion.replace(')','')
        combinacion = combinacion.replace('C','-')
        combinacion = combinacion.replace('R','-')
        combinacion = combinacion.replace('-',',')
        combinacion = combinacion.replace(' ','')
        combinacion = combinacion.split(',')
        for columna in combinacion:
            dato.append(columna)
    
        return dato
    return False
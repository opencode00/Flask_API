import requests as rq
import sys
from datetime import datetime
import common

help ="""
python get_last.py <euro|primi> [# de sorteos anteriores del mes en curso(def: 1, el ultimo)]
"""
"""
comb = last([EMIL|LAPR],num_cmb_ant = 1)
euro = euro_last(comb)
"""
if len(sys.argv) == 1:
    print(help)
    exit()

def last(game_id, num_cmb_ant = 1):
    now = datetime.now()
    init = str(now.month - 1)
    init= f"{now.strftime('%Y')}{init.zfill(2)}01"
    end = str(now.month +1)
    end= f"{now.strftime('%Y')}{end.zfill(2)}01"
    web = f'https://www.loteriasyapuestas.es/servicios/buscadorSorteos?game_id={game_id}&celebrados=true&fechaInicioInclusiva={init}&fechaFinInclusiva={end}'
    response = rq.get(web, headers=common.headers)
    data_raw = response.json()
    return data_raw [:int(num_cmb_ant)]
    
def euro_last(regs):
    data = []
    for item in regs:
        print(common.euro_process(item))
        data.append(common.euro_process(item))

    return data

def primi_last(regs):
    data = []
    for item in regs:
        print(common.primi_process(item))
        data.append(common.primi_process(item))

    return data

def bono_last(regs):
    data = []
    for item in regs:
        print(common.bono_process(item))
        data.append(common.bono_process(item))

    return data

if __name__ == '__main__':
    num_cmb_ant = 1
    if len (sys.argv) > 2:
        num_cmb_ant = sys.argv[2]
    
    if sys.argv[1] == 'euro':
        euro_last(last('EMIL', num_cmb_ant))
    
    if sys.argv[1] == 'primi':
        primi_last(last('LAPR', num_cmb_ant))
from gsheets_creds import get_client
from primitiva_last import primitiva_ayer

client = get_client()
sheet = client.open("Primitiva").sheet1  # Open the spreadhseet

index = sheet.row_count +1
combinacion = primitiva_ayer()

if (combinacion):
    combinacion.append('') #columna K (separador en negro)
    combinacion.append(f'=SUM(C{index}:H{index})')
    combinacion.append(f'=ABS(C{index}-D{index})')
    combinacion.append(f'=ABS(D{index}-E{index})')
    combinacion.append(f'=ABS(E{index}-F{index})')
    combinacion.append(f'=ABS(F{index}-G{index})')
    combinacion.append(f'=ABS(G{index}-H{index})')
    combinacion.append(f'=SUM(M{index}:Q{index})')
    combinacion.append(f'=AVERAGE(M{index}:Q{index})')
    combinacion.append(f'=CONCATENATE(C{index}:H{index})')
    combinacion.append(f'=if(COUNTIF($T$2:T;T{index})>1;COUNTIF($T$2:T;T{index});0)')
    sheet.append_row(combinacion, 'USER_ENTERED', 'INSERT_ROWS', 'A:U')
    # print(combinacion)

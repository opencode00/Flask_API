from gsheets_creds import get_client
from euromillones_last import euromillones_ayer

client = get_client()
sheet = client.open("Euromillones").sheet1  # Open the spreadhseet

index = sheet.row_count +1
combinacion = euromillones_ayer()
if (combinacion):
    combinacion.append(f'=ABS(C{index}-D{index})')
    combinacion.append(f'=ABS(D{index}-E{index})')
    combinacion.append(f'=ABS(E{index}-F{index})')
    combinacion.append(f'=ABS(F{index}-G{index})')
    combinacion.append(f'=if(countif($R$2:$R{index};R{index})>1;1;0)')
    combinacion.append(f'=AVERAGE(C{index}:G{index})')
    combinacion.append(f'=SUM(J{index}:M{index})')
    combinacion.append(f'=AVERAGE(J{index}:M{index})')
    combinacion.append(f'=CONCATENATE(C{index}:G{index})')
    # print(combinacion)
    sheet.append_row(combinacion, 'USER_ENTERED', 'INSERT_ROWS', 'A:J')

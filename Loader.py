import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from openpyxl import load_workbook

fn='result.xlsx'
wb=load_workbook(fn)
list=wb['list']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

CREDENTIALS_FILE = 'testth-413412-a74389de8116.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1u9ooiALTxKPorILlkewQ4Ufd43XM6gy8MXN8UufxIDw' # сохраняем идентификатор файла
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

for i in range(1,list['A2'].value+1):
    if list[f'{alphabet[i]}1'].value == None:
        continue
    elif list[f'{alphabet[i]}1'].value == "HK":
        ranges = [f"{list['A1'].value}!I5:M144"]
        fill='K'
    elif list[f'{alphabet[i]}1'].value == "SZ":
        ranges = [f"{list['A1'].value}!C5:G144"]
        fill='E'
    elif list[f'{alphabet[i]}1'].value == "MSK":
        ranges = [f"{list['A1'].value}!O5:R144"]
        fill='Q'
    else:
        continue

    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    for n in range(2,1000):
        take=list[f'{alphabet[i]}{n}'].value
        #print(take)
        if take == None:
            break
        for l in range(0,139):
            word1, word2, word3 = take.split(' ', 2)
            serch = word1 + ' ' + word2
            redux_main=str(sheet_values[l]).replace(' ','')
            redux_main=redux_main.replace('.','')
            redux_second=serch.replace(' ','')
            if redux_main.lower().find(redux_second.lower()) > 0:
                cell_to_update = f"{list['A1'].value}!{fill}{l+5}"

                # Формирование тела запроса
                request_body = {
                    'values': [
                        [word3]  # Значение для вставки
                    ]
                }

                # Вызов метода spreadsheets().values().update для обновления ячейки
                update_request = service.spreadsheets().values().update(
                    spreadsheetId=spreadsheetId,
                    range=cell_to_update,
                    valueInputOption='USER_ENTERED',
                    body=request_body
                ).execute()

                # Вывод ответа или обработка ошибок
                print(update_request)
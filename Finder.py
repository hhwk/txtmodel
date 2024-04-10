import re
import txt
from openpyxl import load_workbook
message=txt.message
fn='result.xlsx'
wb=load_workbook(fn)
list=wb['list']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=0

x=input('Введите название TG откуда сообщение(Если в сообщение есть название оставьте это поле пустым): ')
if len(x)>0:
    list['A1'] = x

l=message.count('\n\n')
for n in range(1,l+2):
    i = 0
    count=0
    c=message.find('\n\n')
    if c>0:
        c+=1
        tt=message[:c]
        message = message.replace(tt, '')
        tp=tt
    else:
        tt=message
    tt = re.sub(r'\s+', ' ', tt)
    print(tt)

    # Используем регулярные выражения для извлечения информации
    tt=tt.replace('++','GGGG')
    tt=tt.replace('+','GGGGG')
    pattern = r"([A-Za-z0-9]+)\s+(\d+\.?\d*)\s?([A-Za-z]+)\s?(\$?\d+\.?\d*)"
    matches = re.findall(pattern, tt)

    # Выводим извлеченную информацию
    for match in matches:
        product = match[0]
        product = product.replace('GGGGG', '+')
        product=product.replace('GGGG','++')
        quantity = match[1]
        unit = match[2]
        price = match[3]
        price=price.replace('$','')
        if float(price)>100:
            price=float(price)/float(quantity)
        price=str(price).replace('.',',')
        i+=1
        if count==0:
            tl=tt[1:]
            first = tl[:tl.find('\n')]
            first=first.lower()
            if first.find('hong kong')>-1 or first.find('hk')>-1:
                first='HK'
            elif first.find('shenzhen')>-1 or first.find('sz')>-1:
                first='SZ'
            elif first.find('moscow')>-1 or first.find('msk')>-1:
                first='MSK'
            list[f'{alphabet[n]}1']=first
        info=f'{product} {quantity}{unit} {price}'
        list[f'{alphabet[n]}{i+1}'] = info
        #print(i)
list['A2']=n
wb.save(fn)
wb.close()
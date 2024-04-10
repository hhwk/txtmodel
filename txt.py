import re
message = """ HK Stock
🎄12KW water-cooled radiator is more affordable
🍅KA3 166T $3280
🧊Ks0pro $480
🧊KS1 1T $1780
🧊KS2 2T $3480
🍅KS3 7.3T $10600
🍅KS3 8.2T $12000
🍓L7 9050M $4880
🍓S19prohyd 184T $8.1/T
🍓S19Kpro 120T $13.6/T
🍓S19kpro 115T $13.1/T
🍓S19kpro 110T $12.8/T
🍓Z15pro 820K $2000
🍓E9PRO 3580M $2230
🍓E9PRO 3680M $2350

Hong Kong 7 days
⭐️S21 200T $24.5/T
⭐️S21 195T $22.5/T
⭐️S21 188T $21.5/T

10 working days in Hong Kong (10day HK)
🍓L7 8550M $4650
🍓L7 8800M $4750
🍓L7 9050M $4850
🍓L7 9300M $4950
🍓L7 9500M $5160

January 15-30 ICE River 🇭🇰
🧊Ks0pro $399

Shenzhen stock (ShenZhen stock)
🍑M30s++ 106T $9.6/T
🍑M30s++ 108T $9.8/T
🍑M30s++ 110T $9.9/T
🍑M30s++ 112T $10.1/T
🍑M50 118T $11.4/T
🍑M50 120T $11.5/T
🍑M50 122T $11.6/T
🍑S19kpro 115T $13.1/T
🍑S19Kpro 120T $13.8/T

Moscow Stock
🥝E9pro 3680M $2480
🥝S19kpro 115T $1870
🥝S19kpro 120T $2100
🥝S19kpro 120T (GTD)$2260
🥝S19proHyd 184T $1910

Moscow on the way:
(Moscow on the way)
🥝M30s++106T $1210
🥝M50 118T $1580
🥝S19kpro 110T $1710
🥝S19kpro 115T $1780
🥝S19kpro 120T $1930
🥝S19kpro 120T (GTD)$2030
🥝S19kpro 115T (GTD)$1880
🥝L7 9300M $5560
🥝L7 9050M $5360
"""

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "🟥"
        '➡️'
        '✅'
        '⚡'
        '✈'
                           "]+", flags=re.UNICODE)
message=emoji_pattern.sub(r'', message)
rep=['#','- ','Antminer ','IceRIVER ']
for i in range(0,len(rep)):
    message=message.replace(f'{rep[i]}','')
message=message.replace('th','T').replace('mh','M').replace(' TH','T').replace(' MH','M').replace('Mh','M')
message=message.replace(' (ГТД)','').replace(' ( ГТД )','')
for l in range(0,30):
        message=message.replace(f'S{l}Pro hydro',f'S{l}ProHyd').replace(f'S{l}k Pro',f'S{l}kPro').replace(f'S{l}j Pro+',f'S{l}jPro+').replace(f'S{l} XP',f'S{l}XP').replace(f'S{l}pro hyd',f'S{l}ProHyd')
message=message.replace('    ',' ')
message=message.replace('  ',' ')
print(message)

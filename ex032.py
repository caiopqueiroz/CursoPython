ano = int(input('Insira o ano em que estamos. O valor "0" indica o ano atual. '))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} NÃO é um ano bissexto!')
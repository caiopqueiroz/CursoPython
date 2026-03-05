print('\033[34m-'*50)
print('Confederação Nacional de Natação')
print(50*'-')
from datetime import date
atua = date.today().year
nasc = int(input('\033[mAno de nascimento do atleta: '))
idad = atua - nasc
if 100 < idad:
	print('\033[31mAlgo errado\033[m.')
else:
    if 0 < idad <= 9:
        cate = 'MIRIM'
    elif idad <= 14:
        cate = 'INFANTIL'
    elif idad <= 19:
        cate  = 'JUNIOR'
    elif idad <= 25:
        cate = 'SÊNIOR'
    elif idad <= 100:
        cate = 'MASTER'
    print(f'O atleta tem {idad} anos. \n '
          f'A categoria correspondente é: \033[34m{cate}')
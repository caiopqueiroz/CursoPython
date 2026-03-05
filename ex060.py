nume = int(input('Número qualquer: '))
queb = nume
fato = 1
print(f'\n '
      f''
      f'{queb}! =', queb, end=' ')
while nume > 1:
    nume -= 1
    fato *= nume
    print('*', nume, end=' ')
print(f'\n \n O fatorial de \033[33m{queb}\033[m é: \033[34;1;7m {fato * queb} \033[m')

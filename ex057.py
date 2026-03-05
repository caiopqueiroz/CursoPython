sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: (M ou F) ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print('\033[32mEntendido\033[m!')
    else:
        print('\033[31mAlgo errado\033[m.')
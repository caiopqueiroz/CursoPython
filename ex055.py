maio = 0
meno = 0
for anal in range(1, 6):
    peso = float(input(f'Peso em kg da {anal}ª pessoa: '))
    if anal == 1:
        maio = peso
        meno = peso
    else:
        if peso > maio:
            maio = peso
        if peso < meno:
            meno = peso
print(f'\n\033[33;7;1m MAIOR PESO \033[m: {maio} kg \n'
      f'\n\033[33;7;1m MENOR PESO \033[m: {meno} kg')

list = list()
maio = 0
meno = 0
posimaio = 0
posimeno = 0
for cont in range(1, 6):
    list.append(int(input(f'{cont}º valor: ')))
    if cont == 1:
        maio = list[0]
        posimaio = 1
        meno = list[0]
        posimeno = 1
    else:
        if list[cont - 1] > maio:
            maio = list[cont - 1]
            posimaio = cont
        if list[cont - 1] == maio:
            maio = list[cont - 1]
            posimaio = cont
        if list[cont - 1] < meno:
            meno = list[cont - 1]
            posimeno = cont
        if list[cont - 1] < meno:
            meno = list[cont - 1]
            posimeno = cont
print(f'\n\033[1;7m {list} \033[m\n')
print(f'{maio}, na posição {posimaio}, é o valor \033[33;7;1m MAIOR \033[m\n \n'
      f'{meno}, na posição {posimeno}, é o valor \033[33;7;1m MENOR \033[m')
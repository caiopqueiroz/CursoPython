list0 = []
list1 = []
list2 = []
matr = []
somapare = 0
maio = 0
somacolu3 = 0
for cont in range(0, 9):
    valo = int(input('Valor: '))
    if valo % 2 == 0:
        somapare += valo
    if cont == 0 or cont == 1 or cont == 2:
        list0.append(valo)
        if cont == 2:
            somacolu3 += valo
    if cont == 3 or cont == 4 or cont == 5:
        list1.append(valo)
        if cont == 3:
            maio = valo
        else:
            if valo > maio:
                maio = valo
        if cont == 5:
            somacolu3 += valo
    if cont == 6 or cont == 7 or cont == 8:
        list2.append(valo)
        if cont == 8:
            somacolu3 += valo
matr.append(list0[:])
matr.append(list1[:])
matr.append(list2[:])
print(f'\n{matr[0]}\n{matr[1]}\n{matr[2]}')
print(f'\nSOMA DOS VALORES PARES: \033[33;7;1m {somapare} \033[m'
      f'\nSOMA DOS VALORES DA TERCEIRA COLUNA: \033[33;7;1m {somacolu3} \033[m'
      f'\nMAIOR VALOR DA SEGUNDA LINHA: \033[33;7;1m {maio} \033[m')
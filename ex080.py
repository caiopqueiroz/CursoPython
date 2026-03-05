orde = list()
for cont in range(1, 6):
    nume = int(input(f'Digite um valor para a posição {cont}: '))
    if cont == 1 or nume > orde[-1]:
        orde.append(nume)
    else:
        posi = 0
        while posi < len(orde):
            if nume <= orde[posi]:
                orde.insert(posi, nume)
                break
            posi += 1
print(f'\nLista em ordem crescente: \033[33;7;1m {orde} \033[m')
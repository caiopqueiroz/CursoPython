def fato(nume, show=0):
    """
    calcular o fatorial de um número inteiro qualquer
    :param nume: número a ser calculado o fatorial
    :param show: True = mostrar o cálculo / False = mostrar somente o resultado
    :return: resultado final
    """
    if show == 0:
        for cont in range(nume, 1, -1):
            nume *= cont - 1
    elif show == True:
        print(nume, end=' ')
        for cont in range(nume, 1, -1):
            print(f'x {cont - 1}', end=' ')
            nume *= cont - 1
        print(f'= ', end='')
    return nume

valo = int(input('Número inteiro para cálculo do fatorial: '))
perg = str(input('Mostrar cálculo? (S/N) ')).strip().upper()[0]
print('-' * 45)
if perg not in 'N':
    print(f'{fato(valo, True)}')
else:
    print(f'Resultado: {fato(valo)} ')
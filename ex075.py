valo1 = int(input('1º valor: '))
valo2 = int(input('2º valor: '))
valo3 = int(input('3º valor: '))
valo4 = int(input('4º valor: '))
novo = (valo1, valo2, valo3, valo4)
print('\n', novo)
print(f'\nO valor 9 aparece {novo.count(9)} vez(es)')
if 3 in novo:
    print(f'\nO valor 3 aparece, pela primeira vez, na posição {novo.index(3) + 1}')
else:
    print('\nO valor 3 NÃO aparece')
if valo1 % 2 == 0 or valo2 % 2 == 0 or valo3 % 2 == 0 or valo4 % 2 == 0:
    print('\nValor(es) par(es):', end=' ')
    if valo1 % 2 == 0:
        print(valo1, end='  ')
    if valo2 % 2 == 0:
        print(valo2, end='  ')
    if valo3 % 2 == 0:
        print(valo3, end='  ')
    if valo4 % 2 == 0:
        print(valo4)
else:
    print('\nNÃO há valores pares')

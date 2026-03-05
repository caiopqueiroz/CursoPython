from random import randint
cont = 1
conj = ''
maio = 0
meno = 0
while True:
    nume = randint(0, 1000)
    conj += f'{nume}  '
    if cont == 1:
        maio = nume
        meno = nume
    else:
        if nume > maio:
            maio = nume
        if nume < meno:
            meno = nume
    cont += 1
    if cont == 6:
        break
print(conj)
print(f'\n O maior número é {maio}')
print(f' O menor número é {meno}')
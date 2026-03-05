from time import sleep
def maio(nume):
    print('...ANALISANDO VALORES...')
    sleep(2)
    print('Recebi os valores: ', end='')
    for valo in nume:
        print(valo, end='  ', flush=True)
        sleep(0.5)
    print()
    sleep(1)
    print(f'Foram {len(nume)} ao todo.', end=' ')
    if len(nume) > 0:
        print(f'Eu descobri qual o maior! É o {max(nume)}')
    else:
        print()
    sleep(1)


from random import randint
coma = int(input('Quantas sequências criar? '))
print()
for cont in range(0, coma):
    valo2 = list()
    for cont2 in range(0, randint(0,10)):
        valo2.append(randint(-100,100))
    maio(valo2)
    print()
segu = int(input('== PROGRAMA FINALIZADO =='))
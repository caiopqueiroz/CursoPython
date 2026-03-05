from time import sleep
def maio(*nume):
    print('...ANALISANDO VALORES...')
    sleep(2)
    print('Recebi os valores: ', end='')
    for valo in nume:
        print(valo, end='  ')
        sleep(0.5)
    print()
    sleep(1)
    print(f'Foram {len(nume)} ao todo.', end=' ')
    if len(nume) > 0:
        print(f'Eu descobri qual o maior! É o {max(nume)}')
    else:
        print('Não existe maior valor')
    sleep(1)

from random import randint
maio(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print()
maio()
print()
maio(6, 9, 0, 10, 34, 12)
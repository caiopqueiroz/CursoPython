nume = list()
from time import sleep
def sort():
    from random import randint
    for cont in range(0, 5):
        nume.append(randint(0, 10))
    print(f' - A sequência sorteada foi:  ', end='')
    for valo in nume:
        sleep(0.5)
        print(valo, end='   ')
    sleep(0.5)
    print()
def somapar():
    soma = 0
    sleep(0.5)
    print(f' - A soma dos valores pares - ', end='')
    for valo in nume:
        if valo % 2 == 0:
            sleep(0.5)
            print(valo, end=' - ')
            soma += valo
    sleep(0.5)
    print(f'vale {soma}')
def linh():
    print('-' * 40)



sleep(1)
print('== CRIANDO SEQUÊNCIA ==')
linh()
sleep(1)
print('== SOMANDO OS VALORES PARES ==')
linh()
sleep(1)
print('Tudo pronto!')
sort()
somapar()


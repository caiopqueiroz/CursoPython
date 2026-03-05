from time import sleep
def cont(inic, fim, passo):
    for nume in range(inic, fim + 1, passo):
        sleep(0.5)
        print(nume, end='  ')
    sleep(0.5)
    print('FIM!')
def lin():
    print('-' * 40)


cont(1 ,10, 1)
lin()
cont(10, -2, -2)
lin()
sleep(1)
print('Que tal personalizar uma contagem? ')
inic = int(input('Início: '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))
if passo == 0:
    passo = 1
if fim < inic:
    if passo > 0:
        passo -= (passo * 2)
        fim -= 2
    else:
        fim -= 2
lin()
cont(inic, fim, passo)

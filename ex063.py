nume = int(input('Número inteiro: (mínimo 2) '))
print(f'\033[1;7m Os {nume} primeiros termos da Sequência de Fibonacci são: \033[m')
print('0   1', end='   ')
resuante = 0
resu = 1
prox = resuante + resu
quan = 0
while quan < nume - 2:
    print(prox, end='   ')
    resuante = prox - resuante
    resu = prox
    prox = resuante + resu
    quan += 1

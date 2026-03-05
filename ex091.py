from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for cont in range(1, 5):
    jogo[f'Jogador {cont}'] = randint(1,6)
sleep(1)
print('== VALORES SORTEADOS ==')
sleep(1)
for chav, valo in jogo.items():
    print(f' {chav} tirou \033[34m{valo}\033[m no dado')
    sleep(0.5)
rank = []
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('== RESULTADOS FINAIS ==')
sleep(1)
cont2 = 1
for cont2, orde in enumerate(rank):
    if cont2 == 0:
        print(f' {cont2 + 1}º LUGAR: {orde[0]}, que tirou \033[32m{orde[1]}\033[m no dado !PARABÉNS!')
    else:
        print(f' {cont2 + 1}° LUGAR: {orde[0]}, que tirou \033[34m{orde[1]}\033[m no dado')
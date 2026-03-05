print('Esse programa criará palpites para te ajudar! Cada jogo te dará 6 números aleatórios de 1 a 60')
coma = int(input('\nQuantos jogos de MEGA SENA seram gerados? '))
contcoma = 0
jogo = []
conjjogo = []
import random
while True:
    for cont in range(0, 6):
        nume = random.randint(1, 60)
        jogo.append(nume)
        jogo.sort()
    conjjogo.append(jogo[:])
    jogo.clear()
    contcoma += 1
    if coma == contcoma:
        break
for jogo in conjjogo:
    print(f'\n{jogo}\n')



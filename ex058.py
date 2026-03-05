from random import choice
opco = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comp = choice(opco)
resp = -1
erro = 0
print('\033[7;1m Bem-vindo(a) ao novo jogo de adivinhação! \033[m')
print('Eu pensei em um número de 0 a 10. Você consegue adivinhar qual é?')
while resp != comp:
    resp = int(input('Digite aqui seu palpite: '))
    erro += 1
    if resp == comp:
        print(f'\033[32mPARABÉNS!!\033[m \n'
	          f'Você completou o desafio em \033[34;7;1m {erro} \033[m tentativas.')
    elif resp > comp:
        print('\033[31mAinda não...tente um valor \033[31;7;1m menor \033[m')
    else:
        print('\033[31mAinda não...tente um valor \033[31;7;1m maior \033[m')
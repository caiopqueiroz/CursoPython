from random import choice
from time import sleep
print('\033[7;1m Vamos jogar Jokenpô? \033[m')
resp = str(input('Digite aqui: (pedra, papel ou tesoura) ')).strip().title()
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!!')
opco = ['Pedra', 'Papel', 'Tesoura']
maqu = choice(opco)

if maqu == resp:

    print(f'Eu também escolhi \033[34m{maqu.lower()}\033[m. O resultado foi: \033[33mEMPATE\033[m')

else:
    if maqu == 'Pedra':
        if resp == 'Papel':
            venc = 'USUÁRIO'
        elif resp == 'Tesoura':
            venc = 'MÁQUINA'
        else:
            print('\033[31mJOGADA INVÁLIDA\033[m')

    if maqu == 'Papel':
        if resp == 'Pedra':
            venc = 'MÁQUINA'
        elif resp == 'Tesoura':
            venc = 'USUÁRIO'
        else:
            print('\033[31mJOGADA INVÁLIDA\033[m')

    if maqu == 'Tesoura':
        if resp == 'Pedra':
            venc = 'USUÁRIO'
        elif resp == 'Papel':
            venc = 'MÁQUINA'
        else:
            print('\033[31mJOGADA INVÁLIDA\033[m')

    print(f'Eu escolhi \033[34m{maqu.lower()}\033[m! O vencedor é o(a): \033[32m{venc}\033[m')


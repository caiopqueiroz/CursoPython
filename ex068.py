print('\033[7;1m Vamos jogar par ou ímpar!! \033[m')
comp = ''
cont = 0
nume = 0
while True:
    from random import randint
    from time import sleep
    opco = randint(0, 10)
    joga = str(input('\n \033[33;7;1m O que vai escolher? \033[m (\033[34mpar\033[m ou \033[35mímpar\033[m) ')).strip().lower()
    if joga == 'par' or joga == 'p':
        comp = '\033[35mímpar\033[m'
    elif joga == 'impar' or joga == 'ímpar' or joga == 'i':
        comp = '\033[34mpar\033[m'
    else:
        print('\n \033[31;7;1m Algo errado. \033[m')
        break
    print(f'\n Entendi! Eu fico com {comp} então.')
    nume = int(input('\n \033[33;1;7m Quantos dedos vai jogar? \033[m (0 a 10) '))
    print('\n 3...')
    sleep(0.5)
    print('  2...')
    sleep(0.5)
    print('   1...')
    sleep(0.5)
    print(f'\n Eu joguei \033[33;7;1m {opco} \033[m \n Você jogou \033[33;7;1m {nume} \033[m')
    if (opco + nume) % 2 == 0 and comp == '\033[34mpar\033[m':
        print(f' {opco} + {nume} = {opco + nume} \n \n \033[31;1;7m EU VENCI!! \033[m')
    elif (opco + nume) % 2 != 0 and comp == '\033[35mímpar\033[m':
        print(f' {opco} + {nume} = {opco + nume} \n \n \033[31;1;7m EU VENCI!! \033[m')
    else:
        cont += 1
        break
    cont += 1
if (opco + nume) % 2 == 0 and comp == '\033[35mímpar\033[m':
    print(f' {opco} + {nume} = {opco + nume} \n \n \033[32;1;7m PARABÉNS!! Você me venceu! \033[m \n'
          f' Precisou de \033[34;7;1m {cont} \033[m tentativa(s) pra isso.')
if (opco + nume) % 2 != 0 and comp == '\033[34mpar\033[m':
    print(f' {opco} + {nume} = {opco + nume} \n \n \033[32;1;7m PARABÉNS!! Você me venceu! \033[m \n'
          f' Precisou de \033[34;7;1m {cont} \033[m tentativa(s) pra isso.')

val1 = float(input('Primeiro valor: '))
val2 = float(input('Segundo valor: '))
opco = 0
resu = 0
print('-'*50)
print(' [ 1 ] \033[34mSOMAR\033[m \n'
      ' [ 2 ] \033[35mMULTIPLICAR\033[m \n'
      ' [ 3 ] \033[33mDEFINIR O MAIOR\033[m \n'
      ' [ 4 ] \033[32mNOVOS NÚMEROS\033[m \n'
      ' [ 5 ] \033[31mSAIR DO PROGRAMA\033[m')
print('-'*50)
print('O que vamos fazer agora?')
resp = int(input('Digite aqui o número correspondente à sua opção: '))
while resp != 5:
    if resp == 1:
        resu = val1 + val2
        opco = '\033[34mSOMA\033[m'
        resp = 0
    if resp == 2:
        resu = val1 * val2
        opco = '\033[35mMULTIPLICAÇÃO\033[m'
        resp = 0
    if resp == 3:
        if val1 > val2:
            resu = 'O maior valor é o PRIMEIRO'
        elif val2 > val1:
            resu = 'O maior valor é o SEGUNDO'
        elif val1 == val2:
            resu = 'Os dois valores são iguais'
        opco = '\033[33mDEFINIR O MAIOR\033[m'
        resp = 0
    if resp == 4:
        val1 = float(input('\n Primeiro valor: '))
        val2 = float(input(' Segundo valor: '))
        print('-'*50)
        print(' [ 1 ] \033[34mSOMAR\033[m \n'
      		      ' [ 2 ] \033[35mMULTIPLICAR\033[m \n'
      		      ' [ 3 ] \033[33mDEFINIR O MAIOR\033[m \n'
      		      ' [ 4 ] \033[32mNOVOS NÚMEROS\033[m \n'
      		      ' [ 5 ] \033[31mSAIR DO PROGRAMA\033[m')
        print('-'*50)
        resp = int(input('Digite aqui o número correspondente à sua opção: '))
    if resp == 0:
        print(f'\n Você escolheu: {opco} \n'
              f' O seu resultado é: \033[34;7;1m {resu} \033[m')
        rein = str(input('\n Deseja reiniciar o programa? (S ou N) ')).upper().strip()
        if rein == 'S':
            resp = 4
        else:
            resp = 5
if resp == 5:
    print(' \n \033[1;7m PROGRAMA ENCERRADO \033[m')
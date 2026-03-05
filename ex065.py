perg = str(input('Bem-vindo(a)! Deseja escrever um número? (S ou N) ')).upper().strip()
if perg == 'N':
    print('\033[31mFim\033[m')
quan = 0
nume = 0
apoi = nume
maio = 0
meno = 0
if perg == 'S':
    while perg == 'S':
        nume = int(input('\n Digite um valor inteiro: '))
        perg = str(input('Deseja escrever mais um número? (S ou N) ')).strip().upper()
        quan += 1
        apoi += nume
        if quan == 1:
            maio = nume
            meno = nume
        else:
            if nume >= maio:
                maio = nume
            elif nume <= meno:
                meno = nume
    if perg == 'N':
        print('\n Estatísticas finais: ')
        print(f'MÉDIA SIMPLES: \033[34;7;1m {apoi / quan:.2f} \033[m \n'
              f'MAIOR VALOR: \033[34;7;1m {maio} \033[m \n'
              f'MENOR VALOR: \033[34;7;1m {meno} \033[m ')

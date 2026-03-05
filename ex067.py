cont = 1
valo = int(input('Você gostaria de ver a tabuada de qual número? \n'
                 'Se quiser encerrar o programa, basta inserir um valor negativo. '))
if valo > 0:
    print(f'\n \033[33;1;7m Tabuada completa do {valo} \033[m')
while True:
    if valo < 0:
        break
    print(f'  {valo} x {cont} = {valo * cont}')
    cont += 1
    if cont > 9:
        valo = int(input('\n De qual número gostaria de ver agora? '))
        if valo > 0:
            print(f'\n \033[33;1;7m Tabuada completa do {valo} \033[m')
        cont = 1
print('\n \033[7;1m PROGRAMA ENCERRADO \033[m')
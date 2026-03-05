cont = 1
prectota = 0
contcaro = 0
bara = 0
apoi = 1
nomebara = ''

while True:

    nome = str(input(f'\n Nome do {cont}º produto: ')).strip().title()

    prec = float(input(' Preço: R$'))

    prectota += prec

    if prec >= 1000:
        contcaro += 1

    if cont == 1:
        nomebara = nome
        bara = prec
    else:
        if prec < bara:
            bara = prec
            nomebara = nome

    cont += 1

    coma = int(
        input('\n [ 0 ] \033[32mSIM\033[m \n [ 1 ] \033[31mNÃO\033[m \n \n \033[33mQuer continuar?\033[m '))

    if coma == 1:

        break


    elif coma == 0:

        True


    else:

        apoi = 0

        print('\033[31;7;1m Algo errado. \033[m')

        break

if apoi != 0:
    print(f'\n \033[33;7;1m {contcaro} \033[m produto(s) custa(m) mais que R$1000.00 \n \n'
          f' O produto mais barato é o(a) \033[36;7;1m {nomebara} \033[m e custa \033[33;7;1m R${bara:.2f} \033[m \n \n'
          f' \033[33;7;1m TOTAL GASTO NA COMPRA: R${prectota:.2f} \033[m')
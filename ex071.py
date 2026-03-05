print(' \033[1;7m BANCO DINHEIRO INFINITO \033[m')

saqu = int(input('\n Digite aqui o valor que deseja sacar: R$'))
cedu50 = 0
cedu20 = 0
cedu10 = 0
rest = 0

while True:

    if saqu >= 50:
        cedu50 = saqu // 50
        saqu = saqu % 50

    if 50 > saqu >= 20:
        cedu20 = saqu // 20
        saqu = saqu % 20

    if 20 > saqu >= 10:
        cedu10 = saqu // 10
        saqu = saqu % 10

    if 10 > saqu:
        rest = saqu

    break

print(f'\n {cedu50} cédula(s) de R$50.00 \n'
      f' {cedu20} cédula(s) de R$20.00 \n'
      f' {cedu10} cédula(s) de R$10.00 \n'
      f' {rest} cédula(s) de R$1.00 \n')
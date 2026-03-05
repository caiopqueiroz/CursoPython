def fich(n, g):
    print(f'O jogador {n} fez {g} gol(s)')

while True:
    nome = str(input('Nome do jogador: ')).strip().title()
    gols = str(input(f'Quantidade de gols feitos: '))
    print('-' * 50)
    if not gols.isnumeric():
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    fich(nome, gols)
    while True:
        print()
        coma = str(input('Deseja encerrar o programa? (S/N) ')).strip().upper()[0]
        if coma not in 'SN':
            print('!ERRO!')
        else:
            break
    print()
    if coma in 'S':
        break
print('== PROGRAMA ENCERRADO ==')

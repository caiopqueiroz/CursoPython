info = dict()
time = list()
while True:
    info['nome'] = str(input('Nome: ')).title().strip()
    part = int(input(f' Total de partidas que {info['nome']} jogou: '))
    gols = list()
    for cont2 in range(1, part + 1):
        gols.append(int(input(f'  Gols feitos por {info['nome']} na partida {cont2}: ')))
    info['gols'] = gols[:]
    info['total'] = sum(gols)
    time.append(info.copy())
    info.clear()
    gols.clear()
    print()
    while True:
        coma = str(input('Cadastrar outro jogador? (S/N) ')).strip().upper()[0]
        if coma not in 'SN':
            print('\033[31mERRO\033[m')
        else:
            break
    if coma == 'N':
        break
    print()
print()
print(f'cod nome               gols                 total')
print('-' * 50)
for k, info in enumerate(time):
    print(f'{k}', end=' ')
    for valo in info.values():
        print(f'{str(valo):<20}', end=' ')
    print()
print('-' * 50)
print()
while True:
    coma2 = int(input('Mostrar dados de qual jogador? (\033[31m999\033[m pra parar) '))
    if coma2 in range(0, len(time)):
        print()
        print(f'== Histórico do jogador {time[coma2]['nome']} ==')
        for cont3, part in enumerate(time[coma2]['gols']):
            print(f'  - Na partida {cont3 + 1}, fez {part} gols')
        print()
    elif coma2 == 999:
        break
    else:
        print('\033[31mERRO\033[m')
print()
print('== PROGRAMA ENCERRADO ==')
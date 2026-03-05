info = dict()
info['nome'] = str(input('Nome: ')).title().strip()
part = int(input(f' Total de partidas que {info['nome']} jogou: '))
gols = list()
for cont in range(1, part + 1):
    gols.append(int(input(f'  Gols feitos por {info['nome']} na partida {cont}: ')))
info['gols'] = gols
info['total'] = sum(gols)
print('+=' * 30)
print(info)
print('+=' * 30)
for chav, valo in info.items():
    print(f' - {chav} recebeu {valo}')
print('+=' * 30)
print(f'O jogador {info['nome']} jogou {part} partidas:')
for cont, gols in enumerate(info['gols']):
    print(f' - Na partida {cont + 1}, marcou {gols} gols')
print(f'Foi um total de {info['total']} gols')
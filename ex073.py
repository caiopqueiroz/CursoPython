bras = ('zero', 'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo',
        'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atético-MG', 'Santos', 'Corinthians',
        'Vasco da Gama', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude',
        'Sport', 'apoio')

print(f' Os 5 primeiros colocados foram: \n {bras[1: 6]}')

print(f'\n Os 4 últimos colocados foram: \n {bras[-5: -1]}')

print(f'\n Todos os times em ordem alfabética: \n {sorted(bras)}')

print(f'\n O JUVENTUDE está na {bras.index('Juventude')}º posição da tabela')


tabe = ('Nintendo Switch', '2000.00', 'Hollow Knight', '24.00', 'Garrafa térmica', '79.90',
        'Mouse', '55.90', 'Cubo mágico 3d', '20.00', 'Luminária de mesa', '24.90')
print('_'*15, '\033[1;7m TABELA DE PREÇOS \033[m', '_'*15)

print(f'\n{tabe[0]}', end='' '.'*(39 - len(tabe[0])))
print('R$', end='' ' '*(47 - (len(tabe[0]) + len(tabe[1]) + 2 + 36 - len(tabe[0]))))
print(f'{tabe[1]}')

print(f'{tabe[2]}', end='' '.'*(39 - len(tabe[2])))
print('R$', end='' ' '*(47 - (len(tabe[2]) + len(tabe[3]) + 2 + 36 - len(tabe[2]))))
print(f'{tabe[3]}')

print(f'{tabe[4]}', end='' '.'*(39 - len(tabe[4])))
print('R$', end='' ' '*(47 - (len(tabe[4]) + len(tabe[5]) + 2 + 36 - len(tabe[4]))))
print(f'{tabe[5]}')

print(f'{tabe[6]}', end='' '.'*(39 - len(tabe[6])))
print('R$', end='' ' '*(47 - (len(tabe[6]) + len(tabe[7]) + 2 + 36 - len(tabe[6]))))
print(f'{tabe[7]}')

print(f'{tabe[8]}', end='' '.'*(39 - len(tabe[8])))
print('R$', end='' ' '*(47 - (len(tabe[8]) + len(tabe[9]) + 2 + 36 - len(tabe[8]))))
print(f'{tabe[9]}')

print(f'{tabe[10]}', end='' '.'*(39 - len(tabe[10])))
print('R$', end='' ' '*(47 - (len(tabe[10]) + len(tabe[11]) + 2 + 36 - len(tabe[10]))))
print(f'{tabe[11]}\n')

print('_'*50)
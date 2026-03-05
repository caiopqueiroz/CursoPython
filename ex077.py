pala = ('GAROTO', 'TRAVESSO', 'IDADE', 'COMEÇO', 'TROPA', 'CHARLES', 'DIABINHO', 'PASSE', 'ASSASSINO',
        'CRUEL', 'CANETA', 'LETRA', 'ARES', 'BRINCADEIRINHA', 'MALICIA', 'EGOISTA')

print(pala[: 9])
print(pala[9: ])

coma = int(input('\nPosição da palavra: '))

print(f'\n{pala[coma - 1]} possui as vogais:')
if 'A' in pala[coma - 1]:
    print('A', f'{pala[coma - 1].count('A')}x')
if 'E' in pala[coma - 1]:
    print('E', f'{pala[coma - 1].count('E')}x')
if 'I' in pala[coma - 1]:
    print('I', f'{pala[coma - 1].count('I')}x')
if 'O' in pala[coma - 1]:
    print('O', f'{pala[coma - 1].count('O')}x')
if 'U' in pala[coma - 1]:
    print('U', f'{pala[coma - 1].count('U')}x')
indi = dict()
cole = list()
conjidad = list()
while True:
    indi['nome'] = str(input('Nome: ')).strip().title()
    while True:
        indi['sexo'] = str(input(f'Sexo de {indi['nome']}: (M/F) ')).strip().upper()[0]
        if indi['sexo'] not in 'MF':
            print('\033[31mERRO\033[m')
        else:
            break
    indi['idade'] = int(input(f'Idade de {indi['nome']}: '))
    conjidad.append(indi['idade'])
    print()
    cole.append(indi.copy())
    indi.clear()
    while True:
        coma = str(input('Cadastrar outra pessoa? (S/N) ')).strip().upper()[0]
        if coma not in 'SN':
            print('\033[31mERRO\033[m')
        else:
            break
    if coma in 'N':
        break
    print()
print()
print('+=' * 30)
print(f'{len(cole)} pessoas foram cadastradas')
print(f'{sum(conjidad) / len(cole):.1f} é a média de idade do grupo')
print(f'As mulheres cadastradas foram',end='')
for indi in cole:
    if indi['sexo'] == 'F':
        print(f' - {indi['nome']}', end='')
print()
print('Listagem das pessoas acima da média de idade:')
for indi in cole:
    if indi['idade'] > sum(conjidad) / len(cole):
        for chav, valo in indi.items():
            print(f' {chav}: {valo}', end=' /')
        print()
print()
print('== PROGRAMA ENCERRADO ==')

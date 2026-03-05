def nota():
    diar = dict()
    cont = 1
    while True:
        diar[f'nume{cont}'] = float(input(f'Nota do aluno {cont}: '))
        cont += 1
        while True:
            coma = str(input('Cadastrar outra nota? (S/N) ')).strip().upper()[0]
            if coma not in 'SN':
                print('!ERRO!')
            else:
                break
        print()
        if coma in 'N':
            break
    diar['média da turma'] = sum(diar.values()) / len(diar)
    diar['maior nota'] = max(diar.values())
    diar['menor nota'] = min(diar.values())
    diar['total de notas'] = len(diar) - 3
    for chav, valo in diar.items():
        print(f'{chav} recebeu {valo:.2f}')


nota()
def nota(*nume, situ=False):
    """
    função capaz de ler um número qualquer de notas e guardar estatísticas em um dicionário
    (quant / maior nota / menor nota / média / situação(True ou False, parâmetro opcional)
    :param nume: notas
    :param situ: situação(opcional)
    :return: dicionário
    """
    bole = dict()
    bole['quantidade de notas'] = len(nume)
    if len(nume) >= 1:
        bole['maior nota'] = max(nume)
        bole['menor nota'] = min(nume)
        bole['média das notas'] = sum(nume) / len(nume)
        if situ:
            if bole['média das notas'] >= 7:
                bole['situação'] = 'BOA'
            elif bole['média das notas'] <= 5:
                bole['situação'] = 'RUIM'
            else:
                bole['situação'] = 'RAZOÁVEL'
    return bole


resp = nota(2.3, 5.1, 4.75, situ=True)
resp1 = nota(4, 7, 8, 9.5, 10, situ=True)
resp2 = nota(5.25, 6.75, 1.5, 10, 3.4, situ=True)
print(resp)
print()
print(resp1)
print()
print(resp2)
print()
help(nota)
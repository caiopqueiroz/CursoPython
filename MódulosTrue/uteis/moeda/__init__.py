def aume(nume, porc=0, form=True):
    if form:
        return moeda(nume + (nume * porc / 100))
    else:
        return nume + (nume * porc / 100)


def dimi(nume, porc=0, form=True):
    if form:
        return moeda(nume - (nume * porc / 100))
    else:
        return nume - (nume * porc / 100)


def dobr(nume, form=True):
    if form:
        return moeda(nume * 2)
    else:
        return nume * 2


def meta(nume, form=True):
    if form:
        return moeda(nume / 2)
    else:
        return nume / 2


def moeda(nume, moed='R$'):
    return f'{moed}{nume:>8.2f}'.replace('.', ',')


def resu(nume, porcaume=10, porcdimi=10):
    from uteis import estetica
    estetica.linh(40)
    print('== RESUMO DO VALOR =='.center(40))
    estetica.linh(40)
    print(f'Preço analisado:     \t{moeda(nume)}')
    print(f'Dobro do preço:      \t{dobr(nume)}')
    print(f'Metade do preço:     \t{meta(nume)}')
    print(f'Com {porcaume}% de acréscimo: \t{aume(nume, porcaume)}')
    print(f'Com {porcdimi}% de desconto: \t{dimi(nume, porcdimi)}')
    estetica.linh(40)
    print()
def leiaint(mens):
    while True:
        try:
            v = int(input(mens))
        except (ValueError, TypeError):
            print(f'\033[31m!ERRO! Por favor, digite um número válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mValor não inserido\033[m')
            return 0
        else:
            return v


def leiafloa(mens):
    while True:
        try:
            v = float(input(mens).replace(',', '.'))
        except KeyboardInterrupt:
            print('\n\033[31mValor não inserido\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[31m!ERRO! Por favor, digite um número inteiro válido\033[m')
        else:
            return v


def fato(nume):
    for cont in range(nume - 1, 0, -1):
        nume *= cont
    return nume


def dobr(nume):
    return nume * 2


def trip(nume):
    return nume * 3


def mult(nume1, nume2, nume3=1):
    return nume1 * nume2 * nume3
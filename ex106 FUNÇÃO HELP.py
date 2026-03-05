from time import sleep


def ajud(resp):
    help(resp)


def titu(mens, cor):
    print(f'{cor}-' * (len(mens) + 4))
    print(f'  {mens}')
    print('-' * (len(mens) + 4))
    print('\033[m', end='')


while True:
    titu('== SISTEMA DE AJUDA PYTHON ==', '\033[34;7;1m')
    coma = str(input('Função ou biblioteca que deseja saber mais: (Exemplo: print) ')).lower().strip()
    if coma == 'fim':
        titu('== ATÉ MAIS! ==', '\033[35;7;1m')
        break
    titu(f'== BUSCANDO INFORMAÇÕES SOBRE {coma} ==', '\033[33;7;1m')
    sleep(2)
    print('\033[7;1m')
    ajud(coma)
    titu('== DIGITE FIM PARA ENCERRAR O PROGRAMA ==', '\033[31;7;1m')
def novocada(arqu):
    from uteis import numeros
    from uteis import estetica


    estetica.titu('== NOVO CADASTRO ==', 100)
    nome = str(input('Nome: '))
    idad = numeros.leiaint('Idade: ')
    try:
        vali = open(arqu, 'at')
    except:
        print('\033[31m!ERRO! ao abrir o arquivo\033[m')
    else:
        try:
            vali.write(f'{nome};{idad}\n')
        except:
            print('\033[31mHouve um !ERRO! ao adicionar o nome e/ou idade ao arquivo\033[m')
    estetica.titu(f'== REGISTRO DE {nome.upper()} REALIZADO COM SUCESSO! ==', 100)


def menu(tama):
    from uteis import estetica
    from time import sleep
    from uteis import numeros

    sleep(1.5)
    estetica.titu('== OPÇÕES ==', 100)
    for cont, item in enumerate(tama):
        print(f'\t\t\t\t\t\t\t\t  [ \033[34m{cont + 1}\033[m ] \033[33m{item}\033[m')
    estetica.linh(100)
    while True:
        opca = numeros.leiaint('Número da opção desejada: ')
        if 1 <= opca <= len(tama):
            break
        else:
            print('\033[31m!ERRO! Por favor, digite uma opção válida\033[m')
    return opca


def arquexis(arqu):
    try:
        vali = open(arqu, 'rt')
        vali.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaarqu(arqu):
    try:
        vali = open(arqu, 'wt+')
        vali.close()
    except:
        print(f'\033[31mHouve um !ERRO! ao tentar criar o arquivo {arqu}\033[m')
    else:
        print(f'\033[34m...{arqu} criado com sucesso!\033[m')


def lerarqu(arqu):
    from uteis import estetica


    try:
        vali = open(arqu, 'rt')
    except:
        print('\033[31m!ERRO! ao ler o arquivo\033[m')
    else:
        estetica.titu('== PESSOAS CADASTRADAS ==', 100)
        for linh in vali:
            dado = linh.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f' {dado[0]:<30}{dado[1]:>63} anos')


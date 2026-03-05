from uteis import cadastro
from uteis import estetica
from time import sleep


arqu = 'cursoemvídeo.txt'


if not cadastro.arquexis(arqu):
    print('\033[31mArquivo não encontrado!\033[m Criando arquivo...')
    sleep(3)
    cadastro.criaarqu(arqu)
    sleep(3)


cadastro.arquexis(arqu)

estetica.titu('== SISTEMA MODULARIZADO PYTHON v2.0 ==', 100)
while True:
    resp = cadastro.menu(['REALIZAR NOVO CADASTRO', 'MOSTRAR TODOS OS CADASTROS', 'SAIR DO PROGRAMA'] )
    if resp == 1:
        cadastro.novocada(arqu)
    if resp == 2:
        cadastro.lerarqu(arqu)
    elif resp == 3:
        break
estetica.titu('         == \033[31mPROGRAMA ENCERRADO\033[m ==', 100)

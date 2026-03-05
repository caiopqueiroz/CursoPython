from datetime import date
ano = date.today().year


def voto(nasc):
    if nasc >= 18:
        resp = '\033[32mOBRIGATÓRIO\033[m'
    elif nasc == 17 or nasc == 16:
        resp = '\033[33mOPCIONAL\033[m'
    else:
        resp = '\033[31mNEGADO\033[m'
    return resp


perg = int(input('Ano de nascimento: '))
print(f'Com {ano - perg} anos seu status atual para votação é: {voto(ano - perg)}')
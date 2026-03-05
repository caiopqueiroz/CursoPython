#IMPORTANTO ANO DA MÁQUINA
from datetime import date
ano = date.today().year
info = dict()
info['nome'] = str(input('Nome: ')).strip().title()
info['nascimento'] = int(input(f'Ano de nascimento de {info['nome']}: '))
info['ctps'] = int(input('Número da Carteira de Trabalho: (0 = NÃO POSSUI) '))
info['idade'] = ano - info['nascimento']
if info['ctps'] != 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['salário'] = float(input('Salário: R$'))
    info['idade na aposentadoria'] = info['idade'] + (35 - (ano - info['contratação']))
print('+=' * 30)
for chav, valo in info.items():
    print(f' - {chav} recebeu {valo}')